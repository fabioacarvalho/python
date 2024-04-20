from django.db import models

# Create your models here.


class Produto(models.Model):
    pn = models.CharField(verbose_name="PN", max_length=300)
    sn = models.CharField(verbose_name="SN", max_length=300)
    nome = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
