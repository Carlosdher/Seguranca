# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission


#User
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chave_pul = models.TextField()
    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

#Rede
class Canal(CreateUpdateModel):
	sender = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='usuario')
	receber = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='user' )
#Mensagen
class Mensagen(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE)
    email = models.TextField(null=True, blank=True)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE, related_name='canal')



##Mudar a implementação

##Criar cada Chave para usuário

##Chave publica por mensagem

##Export key