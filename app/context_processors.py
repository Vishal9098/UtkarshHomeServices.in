from .models import Cart

def cart_count(request):
    count = 0
    if request.session.session_key:
        count = Cart.objects.filter(
            session_key=request.session.session_key
        ).count()
    return {'cart_count': count}

from .models import Product

def all_services(request):
    services = Product.objects.all()   # 🔥 TEMP: filter hata do
    return {'all_services': services}
