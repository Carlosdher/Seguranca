# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as uno

app_name = 'app'


urlpatterns = [

	path('', uno.Inicial.as_view(), name='Home'),
	path('mensagen', uno.Canal.as_view(), name='sender'),
	path('caixa', uno.CaixaDeEmail.as_view(), name='lista'),
	path('caixa/<pk>/', uno.Email.as_view(), name='mensagen'),
	path('login/', auth_views.LoginView.as_view(template_name='user/auth.html'), name='login')


]