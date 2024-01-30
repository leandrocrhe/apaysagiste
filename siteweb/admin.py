from django.contrib import admin
from .models import Home, Testimonial, Service, Gallery, About, Contact, Form, RepairService, ConcreteService, GarageService, PlatformService, PavingService, CascadesService, PlantingService, PoolService, WallsService, LightingService, BannerPage, ServiceLocation
from modeltranslation.admin import TranslationAdmin


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
  list_display = ('header_decoration', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
  list_display = ('client_name',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }
    
# ========    
# SERVICES
# ========

@admin.register(RepairService)
class RepairService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(ConcreteService)
class ConcreteService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(GarageService)
class GarageService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(PlatformService)
class PlatformService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(PavingService)
class PavingService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(CascadesService)
class CascadesService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(PlantingService)
class PlantingService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(PoolService)
class PoolService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(WallsService)
class WallsService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(LightingService)
class LightingService(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }
    
# ========    
# END SERVICES
# ========

admin.site.register(Gallery)

@admin.register(About)
class AboutAdmin(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
  list_display = ('email', 'phone', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(Form)
class FormAdmin(TranslationAdmin):
  list_display = ('firt_title', 'name', 'last_name',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
    }

@admin.register(BannerPage)
class BannerPageAdmin(TranslationAdmin):
  list_display = ('title', 'id',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
}
    
@admin.register(ServiceLocation)
class ServiceLocationAdmin(TranslationAdmin):
  list_display = ('text',)
  class Media:
    js = (
      'js/jquery-1.9.1.min.js',
      'js/jquery-ui.min.js',
      'js/tabbed_translation_fields.js',
    )
    css = {
    'screen': ('css/tabbed_translation_fields.css',),
}