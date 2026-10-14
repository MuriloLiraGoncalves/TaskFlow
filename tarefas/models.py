from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    prazo = models.DateField(null=True, blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo