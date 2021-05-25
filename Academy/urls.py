
from django.contrib import admin
from django.urls import path

from Academy.views import index_father, ingresar, p_privacidad


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_father),
    path('ingresar/', ingresar),
    path('politicaprivacidad/', p_privacidad),
    
    
    
    ]

