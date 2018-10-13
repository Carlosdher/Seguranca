
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
from . import models, funcoes_crypto
from django.shortcuts import render
import psycopg2, psycopg2.extras



class Cadastro(CreateView):
	model = models.UUIDUser
	template_name = 'user/cadastro.html'
	success_url = reverse_lazy('app:login')
	fields = ['username', 'password']
	
	def form_valid(self, form):
		obj = form.save(commit=False)
		private, public = chaves(2400)
		obj.chave_pul = public
		db = psycopg2.connect("dbname=users user=teste password=testando12 host=127.0.0.1")
		cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute("INSERT INTO private (usuario, chave_privada) VALUES (%s, %s)", (str(self.request.user.id), private))
		cur.close()
		db.close()

		return super(Cadastro, self).form_valid(form)


class Inicial(TemplateView):
	template_name='inicial.html'

class Canal(CreateView):
	model = models.Canal
	template_name = 'sender.html'
	success_url = reverse_lazy('app:sender')
	fields = ['sender', 'receber']


class CaixaDeEmail(ListView):
	models= models.Canal
	template_name = 'lista.html'

	def get_queryset(self):
		return models.Canal.objects.all()

class Email(CreateView):
	model = models.Mensagen
	success_url = reverse_lazy('app:mensagen')
	template_name = 'mensagen.html'
	fields = ['email']

	def post(self, request):
		chave = self.request.user.chave_pul
		mensagen = encrypto(self.request.POST['email'], chave )
		canal = models.Canal.objects.filter(sender=self.request.user)
		texto = models.Mensagen.objects.create(user = self.request.user, canal=canal, texto=mensagen )
		texto.save()


	def get_context_data(self, **kwargs):
		db = psycopg2.connect("dbname=users user=teste password=testando12 host=127.0.0.1")
		cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
		chave_privada = ("FROM chave IMPORT * WHERE usuario= %s")%(self.request.user)
		cur.close()
		db.close()
		lista_mensagens = []
		for mensagen in models.Mensagen.objects.filter(canal__receber=self.request.user):
			lista_mensagens.append(decrypto(mensagen.email, chave_privada))
		kwargs['mensagen'] = lista_mensagens
		return super(Email, self).get_context_data(**kwargs)

	def get_queryset(self):
		return models.Mensagen.objects.all()

			