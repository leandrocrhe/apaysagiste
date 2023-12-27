from siteweb.models import Service, Contact, ServiceLocation


def nav_menu_services(request):
  menu_services = Service.objects.all()
  return {'menu_services': menu_services}

def link_social_media(request):
  urls = Contact.objects.all()
  for link in urls:
    email = link.email
    phone = link.phone
    facebook = link.link_facebook    
    instagram = link.link_instagram
  return {'email': email, 'phone': phone, 'facebook': facebook, 'instagram': instagram}

def location(request):
  siteObj = ServiceLocation.objects.all()
  return {'siteObj': siteObj}
