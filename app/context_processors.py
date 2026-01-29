from .models import Cart

def cart_count(request):
    if request.session.session_key:
        count = Cart.objects.filter(
            session_key=request.session.session_key
        ).count()
    else:
        count = 0

    return {
        'totalitem': count
    }
