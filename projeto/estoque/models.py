from django.db import models

# Create your models here.

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    quantidade_produto = models.IntegerField()
    class Meta:
        verbose_name_plural = "Produtos"

        def __str__(self):
            return self.nome_produto