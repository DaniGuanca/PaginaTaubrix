from django.urls import path
from . import views

#urlpatterns = [
#    path('', views.home),
#    path('servicios', views.servicios, name="servicios"),
#    path('empresa', views.empresa, name="empresa"),
#    path('contacto', views.contacto, name="contacto"),
#]

#Vistas Genericas
urlpatterns = [
    path('', views.Home.as_view()),
    path('servicios', views.Servicios.as_view(), name="servicios"),
    path('empresa', views.Empresa.as_view(), name="empresa"),
    path('contacto', views.Contacto.as_view(), name="contacto"),
]