from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('inicio/',include('inicio.urls')),
    path('', lambda request: redirect('lista_clientes'), name='home'),
]