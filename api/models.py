from django.db import models
from django.contrib.auth.models import AbstractUser
from user.models import User


class Demanda(models.Model):

    descricao = models.CharField(max_length=150, verbose_name="descrição")
    endereco = models.CharField(max_length=60, verbose_name="endereço")
    contato = models.CharField(max_length=60)
    anunciante = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.descricao, self.anunciante.email)
