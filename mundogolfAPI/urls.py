from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Core Views
    url(r'^admin/', admin.site.urls),
    # CRM Views
    url(r'^solicitud/', include("apps.solicitudes.urls", namespace='solicitudes')),  
]
