from django.db import models


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    categoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    url = models.URLField(blank=False, null=False)
