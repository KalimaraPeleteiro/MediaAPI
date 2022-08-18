from django.db import models


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    url = models.URLField(blank=False, null=False)
