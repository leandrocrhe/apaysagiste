from .models import Home, Testimonial, Service, Gallery, About, Contact, Form, RepairService, ConcreteService, GarageService, PlatformService, PavingService, CascadesService, PlantingService, PoolService, WallsService, LightingService, BannerPage, ServiceLocation
from modeltranslation.translator import TranslationOptions, translator, register

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('header_decoration', 'header_title', 'header_span', 'header_text', 'header_button', 'warranty_title', 'warranty_span', 'warranty_subtitle_estimate', 'warranty_text_estimate', 'warranty_subtitle_warranty', 'warranty_text_warranty', 'warranty_button', 'service_title', 'service_span', 'service_text', 'testimonials_title',)

@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('client_charge',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_detail',)
    
# SERVICES
@register(RepairService)
class BannerPageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(ConcreteService)
class ConcreteServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(GarageService)
class GarageServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(PlatformService)
class PlatformServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(PavingService)
class PavingServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(CascadesService)
class CascadesServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(PlantingService)
class PlantingServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(PoolService)
class PoolServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(WallsService)
class WallsServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
@register(LightingService)
class LightingServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)
    
# END SERVICES

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'short_text', 'long_text',)

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('info_form', 'text_social_networks', 'text_direct_contact', 'email_title', 'phone_title',)

@register(Form)
class FormTranslationOptions(TranslationOptions):
    fields = ('firt_title', 'name', 'last_name', 'phone', 'mail', 'secound_title', 'address', 'app', 'city', 'postal_code', 'third_title', 'details', 'submit',)
    
@register(BannerPage)
class BannerPageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',)
    
@register(ServiceLocation)
class ServiceLocationTranslationOptions(TranslationOptions):
    fields = ('text', 'text_locations',)