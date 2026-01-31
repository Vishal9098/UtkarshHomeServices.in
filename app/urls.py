from django.urls import path 
from app import views 
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView
# from .forms import LoginForm, CustomPasswordChangeForm

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import gallery
from .views import blogs 

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('address/', views.address, name='address'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('search/<str:query>/', views.search, name='search'),
    path('gallery/', gallery, name='gallery'),
    path("blogs/", blogs, name="blogs"),   
    path('checkout/', views.checkout, name='checkout'),
    path('order-place/', views.order_place, name='order_place'),
    path('cart/', views.show_cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('orders/', views.orders, name='orders'),

        
    # path('orders/', views.orders, name='orders'), 
    path('orders/', views.orders, name='orders'),
    path('accepted-orders/', views.accepted_orders, name='accepted_orders'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),

    path('', views.ProductView.as_view(), name='home'),
    path('orders/', views.orders, name='orders'),
    path('accepted-orders/', views.accepted_orders, name='accepted_orders'),
    # path('accept-order/<int:order_id>/', views.accept_order, name='accept_order'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('accept-order/<int:order_id>/', views.accept_order, name='accept_order'),
    path('remove-cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('product/<int:pk>/review/', views.add_review, name='add-review'),
    path('plus-cart/<int:cart_id>/', views.plus_cart, name='plus_cart'),
    path('minus-cart/<int:cart_id>/', views.minus_cart, name='minus_cart'),

















  
  




 

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)














































































































































