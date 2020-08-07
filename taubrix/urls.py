from django.urls import path
from . import views

# Vistas Genericas
urlpatterns = [
    path('', views.Home.as_view()),
    path('servicios', views.Servicios.as_view(), name="servicios"),
    path('empresa', views.Empresa.as_view(), name="empresa"),
    path('contacto', views.Contacto.as_view(), name="contacto"),
]
