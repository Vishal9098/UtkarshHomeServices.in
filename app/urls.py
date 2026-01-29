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
#     path('pluscart/', views.plus_cart),
#     path('minuscart/', views.minus_cart),
#     path('removecart/', views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('address/', views.address, name='address'),
#     path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),

  
    path('search/', views.search, name='search'),
#     path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
#     path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class= CustomPasswordChangeForm), name='passwordchange'),
#     path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
#     path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/', views.search, name='search'),
    path('search/<str:query>/', views.search, name='search'),
    path('gallery/', gallery, name='gallery'),
    path("blogs/", blogs, name="blogs"),   
   
    # path("villa-cleaning/", villa_cleaning, name="villa_cleaning"),

    # path('orders/', views.orders, name='orders'),

    path('checkout/', views.checkout, name='checkout'),
    path('order-place/', views.order_place, name='order_place'),
    # path('orders/', views.orders, name='orders'),
#     path('pluscart/', views.plus_cart, name='pluscart'),
#     path('minuscart/', views.minus_cart, name='minuscart'),
#     path('removecart/', views.remove_cart, name='removecart'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('minuscart/', views.minuscart, name='minuscart'),
    path('removecart/', views.removecart, name='removecart'),
    path('cart/', views.show_cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    
    path('orders/', views.orders, name='orders'), 











  
  




 

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







































































































