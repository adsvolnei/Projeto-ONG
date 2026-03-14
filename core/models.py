from django.db import models

# Create your models here.
from django.db import models

class Familia(models.Model):
    nome_responsavel = models.CharField(max_length=100, verbose_name="Nome do Responsável")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    def __str__(self):
        return self.nome_responsavel