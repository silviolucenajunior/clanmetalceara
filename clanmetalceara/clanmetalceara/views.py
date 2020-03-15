from django.shortcuts import render
from modulos.evento.models import Evento


def home_view(request):
  eventos = Evento.objects.all()
  template = 'home.html'
  context = {'eventos': eventos}
  return render (request, template, context)