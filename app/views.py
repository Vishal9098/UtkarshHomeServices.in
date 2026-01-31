from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import (
    Product,
    Cart,
    ServicePrice,
    Customer,
    OrderPlaced,
    Review
)

# ----------------------------------
# HOME / PRODUCT LIST
# ----------------------------------
class ProductView(View):
    def get(self, request):
        totalitem = 0
        if request.session.session_key:
            totalitem = Cart.objects.filter(
                session_key=request.session.session_key
            ).count()

        return render(request, 'app/home.html', {
            'topwears': Product.objects.filter(category='TW'),
            'bottomwears': Product.objects.filter(category='BW'),
            'mobiles': Product.objects.filter(category='M'),
            'totalitem': totalitem
        })


# ----------------------------------
# PRODUCT DETAIL
# ----------------------------------
class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        item_already_in_cart = False
        if request.session.session_key:
            item_already_in_cart = Cart.objects.filter(
                product=product,
                session_key=request.session.session_key
            ).exists()

        reviews = Review.objects.filter(product=product).order_by('-created_at')

        return render(request, 'app/productdetail.html', {
            'product': product,
            'item_already_in_cart': item_already_in_cart,
            'reviews': reviews
        })


# ----------------------------------
# ADD TO CART
# ----------------------------------
def add_to_cart(request):
    prod_id = request.GET.get("prod_id")
    price_id = request.GET.get("price_id")

    if not request.session.session_key:
        request.session.create()

    product = get_object_or_404(Product, id=prod_id)

    service_price = None
    if product.is_service:
        if not price_id:
            messages.error(request, "Please select a service option")
            return redirect('product-detail', pk=product.id)
        service_price = get_object_or_404(ServicePrice, id=price_id)

    Cart.objects.create(
        session_key=request.session.session_key,
        product=product,
        service_price=service_price
    )

    return redirect("showcart")


# ----------------------------------
# SHOW CART  ✅ (NO EXTRA CHARGE)
# ----------------------------------
def show_cart(request):
    carts = Cart.objects.filter(session_key=request.session.session_key)
    totalamount = sum(c.total_price for c in carts)

    return render(request, 'app/cart.html', {
        'carts': carts,
        'totalamount': totalamount
    })


# ----------------------------------
# CHECKOUT  ✅ (SAME TOTAL)
# ----------------------------------
def checkout(request):
    carts = Cart.objects.filter(session_key=request.session.session_key)
    totalamount = sum(c.total_price for c in carts)

    return render(request, 'app/checkout.html', {
        'carts': carts,
        'totalamount': totalamount
    })


# ----------------------------------
# PLACE ORDER
# ----------------------------------
def order_place(request):
    carts = Cart.objects.filter(session_key=request.session.session_key)

    if not carts.exists():
        return redirect('showcart')

    customer = Customer.objects.create(
        name=request.POST.get('name'),
        mobile=request.POST.get('mobile'),
        address=request.POST.get('address')
    )

    for c in carts:
        OrderPlaced.objects.create(
            customer=customer,
            product=c.product,
            quantity=c.quantity,
            price=c.total_price
        )
        c.delete()

    return redirect('orders')


# ----------------------------------
# REMOVE CART ITEM
# ----------------------------------
def remove_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return redirect('showcart')


# ----------------------------------
# ORDERS
# ----------------------------------
def orders(request):
    orders = OrderPlaced.objects.filter(
        status='pending'
    ).order_by('-ordered_at')

    return render(request, 'app/orders.html', {
        'order_placed': orders
    })


def accepted_orders(request):
    orders = OrderPlaced.objects.filter(
        status='accepted'
    ).order_by('-ordered_at')

    return render(request, 'app/accepted_orders.html', {
        'orders': orders
    })


def accept_order(request, order_id):
    order = get_object_or_404(OrderPlaced, id=order_id)
    order.status = 'accepted'
    order.save()
    return redirect('orders')


def cancel_order(request, order_id):
    order = get_object_or_404(OrderPlaced, id=order_id)
    order.status = 'pending'
    order.save()
    return redirect('orders')


# ----------------------------------
# ADD / UPDATE REVIEW
# ----------------------------------
@login_required
def add_review(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)

        Review.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={
                'rating': request.POST.get('rating'),
                'comment': request.POST.get('comment')
            }
        )

    return redirect('product-detail', pk=pk)

def gallery(request):
    return render(request, 'app/gallery.html')



def blogs(request):
    data = {
        "latest": [
            {
                "title": "House Cleaning Services Near Me",
                "desc": "House Cleaning Services Near Me: 9 Myths People Believe",
                "date": "2021-10-14"
            },
            {
                "title": "Kitchen Cleaning Services",
                "desc": "Kitchen Cleaning Services: 11 Signs Your Kitchen Needs Deep Cleaning",
                "date": "2021-09-11"
            }
        ],
        "sections": [
            {
                "name": "Office Cleaning",
                "posts": [
                    {"title": "Why Smart Businesses Now Prioritize Professional Office Cleaning Services"},
                    {"title": "How the Urban Service Providers are Changing the Way of Living"},
                    {"title": "What are the Points to Consider While Hiring Professional Deep Cleaning"}
                ]
            },
            {
                "name": "Pest Control",
                "posts": [
                    {"title": "5 Benefits of Hiring a Commercial Pest Control Company"},
                    {"title": "How long does pest control service last?"},
                    {"title": "5 ways to keep your children safe from bug bites"}
                ]
            },
            {
                "name": "Electricians",
                "posts": [
                    {"title": "Create an Aesthetic Room with LED Lights"},
                    {"title": "How to protect home appliances from voltage fluctuation?"},
                    {"title": "How to Fix Noise Coming from a High Speed Ceiling Fan"}
                ]
            }
        ]
    }

    return render(request, "app/blogs.html", data)

def address(request):  
    totalitem = 0
    if request.session.session_key:
        totalitem = Cart.objects.filter(
            session_key=request.session.session_key
        ).count()

    add = Customer.objects.all()
    return render(
        request,
        'app/address.html',
        {'add': add, 'active': 'btn-primary', 'totalitem': totalitem}
    )



def search(request):
    query = request.GET.get('query')
    products = []
    if query:
        products = Product.objects.filter(title__icontains=query)
    return render(request, 'app/search.html', {'products': products, 'query': query})


def plus_cart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.quantity += 1
    cart.save()
    return redirect('cart')


def minus_cart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    return redirect('cart')




























