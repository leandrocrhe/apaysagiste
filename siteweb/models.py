from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db.models.signals import pre_delete
import cloudinary


class Home(models.Model):
    header_decoration = models.CharField(max_length=100)
    header_title = models.CharField(max_length=100)
    header_span = models.CharField(max_length=100)
    header_text = models.TextField()
    header_button = models.CharField(max_length=20)
    warranty_title = models.CharField(max_length=100)
    warranty_span = models.CharField(max_length=100)
    warranty_subtitle_estimate = models.CharField(max_length=100)
    warranty_text_estimate = models.TextField()
    warranty_subtitle_warranty = models.CharField(max_length=100)
    warranty_text_warranty = models.TextField()
    warranty_button = models.CharField(max_length=80, default="warranty button contact estimate")
    service_title = models.CharField(max_length=100, default="service title")
    service_span = models.CharField(max_length=100, default="service title span")
    service_text = models.TextField(default="service text paragraph")
    testimonials_title = models.CharField(max_length=50, default='Testimonials')
    background = models.ImageField(upload_to='home', null=True)

class Testimonial(models.Model):
    testimonial = models.TextField(max_length=562)
    client_name = models.CharField(max_length=50)
    client_charge = models.CharField(max_length=50, default="Client")

class Service(models.Model):
    title = models.CharField(max_length=50, default='Service')
    description = models.TextField(max_length=150, blank=True)
    banner = models.ImageField(upload_to='banner', null=True)
    url = models.CharField(max_length=25, blank=True)
    button_detail = models.CharField(max_length=18, verbose_name='View details button', default="View details")
    identificador = models.CharField(max_length=20, blank=True)
    

# SERVICES        
class RepairService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/repair', null=True, blank=True)
        
class ConcreteService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/concrete', null=True, blank=True)
        
class GarageService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/garage', null=True, blank=True)
        
class PlatformService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/platform', null=True, blank=True)
    
class PavingService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/pavers_asphalt', null=True, blank=True)
    
class CascadesService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/cascades_chimneys', null=True, blank=True)
    
class PlantingService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/lawn_planting', null=True, blank=True)
    
class PoolService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/pool', null=True, blank=True)
    
class WallsService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/walls', null=True, blank=True)
    
class LightingService(models.Model):
    title = models.CharField(max_length=60, default="Title Name")
    subtitle = models.CharField(max_length=100, default="Text of Subtitle", blank=True)
    description = models.TextField(default="Descriptive text of this topic")
    thumbnail = models.ImageField(upload_to='services/lighting', null=True, blank=True)

# END SERVICES

class Gallery(models.Model):
    images = models.ImageField(upload_to='gallery')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)    

    def __str__(self):
        return timezone.localtime(self.created_at).strftime('%Y-%m-%d %H:%M:%S')
    
@receiver(pre_delete, sender=Gallery)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.images.public_id)
    

class About(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField(blank=True)
    short_text = models.TextField(default='A small paragraph')
    long_text = models.TextField(default='A more long text')
    images = models.FileField(upload_to='about', null=True, blank=True, storage=RawMediaCloudinaryStorage())
    

class Contact(models.Model):
    info_form = models.TextField(max_length=100, blank=True)
    text_social_networks = models.CharField(max_length=50, default='Connect with us on social networks')
    text_direct_contact = models.CharField(max_length=50, default='Contact Us Directly')
    email_title = models.CharField(max_length=20, default='Email')
    email = models.CharField(max_length=50, blank=True)
    phone_title = models.CharField(max_length=20, default='Phone')
    phone = models.CharField(max_length=20, blank=True)
    link_facebook = models.URLField(default='https://www.facebook.com/')
    link_instagram = models.URLField(default='https://www.instagram.com/')

class Form(models.Model):
    firt_title = models.CharField(max_length=30)
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    mail = models.CharField(max_length=10)
    secound_title = models.CharField(max_length=30)
    address = models.CharField(max_length=10)
    app = models.CharField(max_length=12)
    city = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=15)
    third_title = models.CharField(max_length=60)
    details = models.CharField(max_length=10)
    submit = models.CharField(max_length=15)
    
class BannerPage(models.Model):
    title = models.CharField(max_length=50, default="Title Name")
    subtitle = models.TextField(max_length=150, blank=True)
    banner = models.ImageField(upload_to='banner', blank=True)
    identificador = models.CharField(max_length=20, blank=True)
    
    
class ServiceLocation(models.Model):
    text = models.CharField(max_length=60, default="Landscaping expert in downtown Quebec City")
    text_locations = models.TextField()
    

