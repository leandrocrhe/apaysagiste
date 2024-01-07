"""
URL configuration for apaysagiste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from siteweb import views
# from siteweb.models import Service

# services = Service.objects.all()
# for service in services:
#     print(f"path('{service.title}/', views.services, name='{service.title}')")

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('testimonial/', views.testimonial, name='testimonial'),
    
    #services
    path('repair/', views.services01, name='repair'),
    path('concrete/', views.services02, name='concrete'),
    path('garages/', views.services03, name='garages'),
    path('platforms/', views.services04, name='platforms'),
    path('pavers_asphalt/', views.services05, name='pavers_asphalt'),
    path('waterfalls_chimneys/', views.services06, name='waterfalls_chimneys'),
    path('lawn_plantation/', views.services07, name='lawn_plantation'),
    path('pool_edging/', views.services08, name='pool_edging'),
    path('walls/', views.services09, name='walls'),
    path('lighting/', views.services10, name='lighting'),
    #servicesEnd
        
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.uploadMultiImgs, name='uploadMultiImgs'),
    path('delete_image/<int:img_id>/', views.delete_image, name='delete_image'),    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('mail/', views.sendemail, name='sendemail'),
    
    #preview services
    path('preview/', views.preview, name='preview'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path('set_language/<str:language>', views.set_language, name='set_language'),
]
