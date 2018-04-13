from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

### IMPORT ###
from .views import *

app_name = "solicitudes"

urlpatterns = [
	url(r'^$', solicitud, name="solicitud"), # Ver todas las facturas
]

