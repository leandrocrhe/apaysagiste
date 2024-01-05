from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import translation
from siteweb.models import Home, Testimonial, Service, Gallery, About, Contact, Form, RepairService, ConcreteService, GarageService, PlatformService, PavingService, CascadesService, PlantingService, PoolService, WallsService, LightingService, BannerPage
from urllib.parse import urlparse
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
import uuid
from django.core.exceptions import ValidationError
from django.contrib import messages


def set_language(request, language):
	for lang, _ in settings.LANGUAGES:
		translation.activate(lang)
		try:
			view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
		except Resolver404:
			view = None
		if view:
			break
	if view:
		translation.activate(language)
		next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
		response = HttpResponseRedirect(next_url)
		response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
	else:
		response = HttpResponseRedirect("/")
	return response

def home(request):   
    homes = Home.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'homes': homes, 'services': services, 'testimonials': testimonials})

def testimonial(request):
    homes = Home.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial.html', {'testimonials': testimonials, 'homes': homes})

def preview(request):
    homes = Home.objects.all()
    services = Service.objects.all()
    return render(request, 'services_gallery.html', {'services': services, 'homes': homes})

def identificador(name, obj):
    thisObject = obj.objects.all()
    for object in thisObject:
        if object.identificador == name:
            return object

# SERVICES
def services01(request):
    services = RepairService.objects.all()
    modelo = RepairService.__name__.lower()
    thisService = identificador('repair', Service)   
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services02(request):
    services = ConcreteService.objects.all()
    modelo = ConcreteService.__name__.lower()
    thisService = identificador('concrete', Service)
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services03(request):
    services = GarageService.objects.all()
    modelo = GarageService.__name__.lower()
    thisService = identificador('garages', Service)
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services04(request):
    services = PlatformService.objects.all()
    modelo = PlatformService.__name__.lower()
    thisService = identificador('platforms', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services05(request):
    services = PavingService.objects.all()
    modelo = PavingService.__name__.lower()
    thisService = identificador('pavers_asphalt', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services06(request):
    services = CascadesService.objects.all()
    modelo = CascadesService.__name__.lower()
    thisService = identificador('waterfalls_chimneys', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services07(request):
    services = PlantingService.objects.all()
    modelo = PlantingService.__name__.lower()
    thisService = identificador('lawn_plantation', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services08(request):
    services = PoolService.objects.all()
    modelo = PoolService.__name__.lower()
    thisService = identificador('pool_edging', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services09(request):
    services = WallsService.objects.all()
    modelo = WallsService.__name__.lower()
    thisService = identificador('walls', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

def services10(request):
    services = LightingService.objects.all()
    modelo = LightingService.__name__.lower()
    thisService = identificador('lighting', Service)    
    return render(request, 'services.html', {'thisService': thisService, 'services': services, 'modelo': modelo})

# END SERVICES

def gallery(request):
    images = Gallery.objects.all()
    thisService = identificador('gallery', BannerPage)    
    print(thisService)
    return render(request, 'gallery.html', {'thisService': thisService, 'images': images})

def uploadMultiImgs(request):
    if request.method == "POST":
        try:
            images = request.FILES.getlist('images')
            for image in images:
                # Obtener el nombre original del archivo
                original_filename = image.name                
                # Generar un nuevo nombre de archivo con un UUID aleatorio
                unique_filename = str(uuid.uuid4()) + "_" + original_filename                
                # Asignar el nuevo nombre al archivo
                image.name = unique_filename                
                # Guardar la imagen en el sistema de archivos
                Gallery.objects.create(images=image)
        except (IOError, ValidationError) as e:
            # Manejar la excepción, por ejemplo, imprimir un mensaje de error o redirigir a una página de error.
            print(f"Error al procesar archivos: {e}")
    return redirect('gallery')




# def delete_image(request, pk):
#     images = get_object_or_404(Gallery, pk=pk)
#     images = Gallery.objects.get(pk=pk)
#     print(images)
#     images.delete()
#     return redirect('/gallery/')




def about(request):
    about_us = About.objects.all()    
    banner = identificador('about', BannerPage)
    return render(request, 'about.html', {'about_us': about_us, 'banner': banner})

def contact(request):
    banner = identificador('contact', BannerPage)
    forms = Form.objects.all()
    contactus = Contact.objects.all()
    return render(request, 'contact.html', {'banner': banner, 'forms': forms, 'contactus': contactus})

def sendemail(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        apellidos = request.POST['lastname']
        telefono = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        app = request.POST['apto']
        city = request.POST['city']
        cpostal = request.POST['cpostal']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        # email_to = ['leandrocrhe@gmail.com']
        email_to = ['pavepuig@outlook.com']        
        
        html_message = f'<strong>Nombre del cliente:</strong> {name} {apellidos}<br>' \
                       f'<strong>Teléfono:</strong> {telefono}<br>' \
                       f'<strong>Correo Electrónico:</strong> {email}<br>' \
                       f'<strong>Dirección:</strong> {address}.<br>' \
                       f'<strong>Apartamento:</strong> {app}<br>' \
                       f'<strong>Ciudad:</strong> {city}<br>' \
                       f'<strong>Código Postal:</strong> {cpostal}<br><br>' \
                       f'<strong>Detalles del Proyecto:</strong><br>{message}'
        
        try:
            send_mail(
                'Cliente APaysagiste',
                '',
                email_from,
                email_to,
                fail_silently=False,
                html_message=html_message
            )                
            messages.success(request, "Mail sent successfully")
        except Exception as e:
            messages.error(request, f"Error sending mail: {str(e)}")
            
    return redirect('contact')
