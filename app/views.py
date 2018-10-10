
# -*- coding: utf-8 -*-
from django.views.generic import View

from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse



from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from django.shortcuts import render


class Inicial(TemplateView):
	template_name='inicial.html'

class Canal(CreateView):
	model = models.Canal
	template_name = 'sender.html'
	success_url = reverse_lazy('app:sender')
	fields = ['sender', 'receber', 'key_pul']

class CaixaDeEmail(ListView):
	models= models.Mensagen
	template_name = 'lista.html'

	def get_queryset(self):
		return models.Mensagen.objects.filter(canal__receber=self.request.user)

class Email(DetailView):
	model = models.Canal
	template_name = 'mensagen.html'

	def get_queryset(self):
		if 'Enviar' in self.request.POST :
			models.Mensagen.objects.create(email = self.request.POST['email'], canal=self.request.Canal, key_p='teste')
		return models.Mensagen.objects.filter(canal=self.request.Canal)