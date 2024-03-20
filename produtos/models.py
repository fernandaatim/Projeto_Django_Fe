from django.db import models

class Produtos(models.Model):
    descricao = models.CharField(max_lenght=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
