from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('outcome/', views.outcome, name='outcome'),
    path('service/', views.service, name='service'),
    path('innovation/', views.innovation, name='innovation'),
    path('login/', views.userlogin, name='userlogin'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
