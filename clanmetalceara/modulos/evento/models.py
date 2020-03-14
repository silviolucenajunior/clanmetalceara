from django.db import models

class Evento(models.Model):
  data_realizacao = models.DateTimeField(blank = True, null = True)
  flyer = models.ImageField(upload_to = 'eventos/%Y/%m/', blank = True, null = True)
  local = models.ForeignKey('Local', on_delete = models.SET_NULL, blank = True, null = True)
  nome = models.CharField(max_length = 128)

  data_criado = models.DateTimeField(blank = True, null = True)
  data_editado = models.DateTimeField(blank = True, null = True)
  deletado = models.BooleanField()

class Local(models.Model):
  bairro = models.CharField(max_length = 255, blank = True, null = True)
  cidade = models.CharField(max_length = 255, blank = True, null = True)
  endereco = models.CharField(max_length =  255, blank = True, null = True)
  fachada = models.ImageField(upload_to = 'local-evento/', blank = True, null = True)
  latitude = models.DecimalField(max_digits = 9, decimal_places = 6, blank = True, null = True)
  longitude = models.DecimalField(max_digits = 9, decimal_places = 6, blank = True, null = True)

  data_criado = models.DateTimeField()
  data_editado = models.DateTimeField()
  deletado = models.BooleanField()
