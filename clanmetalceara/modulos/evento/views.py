from django.shortcuts import render

def home_view(request):
  template = 'home.html'
  context = {'eventos': ()}
  return render (request, template, context)
