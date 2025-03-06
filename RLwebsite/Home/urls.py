from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('outcome/', views.outcome, name='outcome'),
    path('service/', views.service, name='service'),
    path('innovation/', views.innovation, name='innovation'),
    path('login/', views.userlogin, name='userlogin'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/update/<str:product_name>/', views.update_cart, name='update_cart'),
    path('cart/remove/<str:product_name>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
