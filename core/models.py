from unittest.util import _MAX_LENGTH
from django.db import models


class Genero(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Gravadora(models.Model):
    nome = models.CharField(max_length=200)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Artista(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Artistas"


class Musica(models.Model):
    Título = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32)
    Tempos = models.IntegerField()
    categoria = models.ForeignKey(
        Genero, on_delete=models.PROTECT, related_name="livros"
    )
    Gavadora = models.ForeignKey(
        Gravadora, on_delete=models.PROTECT, related_name="livros"
    )
    tempo = models.TimeField(max_length=4)
    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
