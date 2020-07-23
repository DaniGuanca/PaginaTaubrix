from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import FormContacto
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages


# Create your views here.
from .models import Texto, Integrante, Imagen


class Home(generic.ListView):
    template_name = "taubrix/index.html"
    context_object_name = "lista_textos"

    def get_queryset(self):
        return Texto.objects.filter(nombre__icontains="indice")


class Servicios(generic.ListView):
    template_name = "taubrix/servicios.html"
    context_object_name = "lista_textos"

    def get_queryset(self):
        return Texto.objects.filter(nombre__icontains='servicio')


class Empresa(generic.ListView):
    template_name = "taubrix/empresa.html"
    context_object_name = "lista_textos"

    def get_queryset(self):
        return Texto.objects.filter(nombre__icontains='empresa')

    def get_context_data(self, **kwargs):
        context = super(Empresa, self).get_context_data(**kwargs)

        context['lista_integrantes'] = Integrante.objects.all()

        return context


class Contacto(generic.ListView):
    template_name = "taubrix/contacto.html"
    context_object_name = "lista_textos"

    def get_queryset(self):
        return Texto.objects.filter(nombre__icontains='contacto')

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        asunto = request.POST.get("asunto")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        if (not nombre.strip()) or (not apellido.strip()) or (not asunto.strip()) or (not email.strip()) or (not mensaje.strip()):
            messages.error(request, 'Complete todos los campos')
        else:

            body = render_to_string(
                'taubrix/contenido_email.html', {
                    'nombre': nombre,
                    'apellido' : apellido,
                    'email': email,
                    'mensaje': mensaje,
                },
            )

            mensaje_email = EmailMessage(
                subject=asunto,
                body=body,
                from_email=email,
                to=['taubrix.arg@gmail.com'],
            )
            mensaje_email.content_subtype = 'html'

            try:
                mensaje_email.send()
                messages.success(request, 'Correo enviado con éxito.')
            except Exception as e:
                messages.error(request, 'Ocurrió un error al enviar el correo.')
        return redirect('contacto')
