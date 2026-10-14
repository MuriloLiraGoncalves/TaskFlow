
from django.test import TestCase
from django.urls import reverse
from .models import Tarefa


class TaskFlowTests(TestCase):

    def test_pagina_inicial_carrega(self):
        resposta = self.client.get(reverse("lista_tarefas"))
        self.assertEqual(resposta.status_code, 200)

    def test_cadastrar_tarefa(self):
        resposta = self.client.post(
            reverse("lista_tarefas"),
            {
                "titulo": "Estudar arquitetura MVC",
                "descricao": "Preparar o relatório",
                "prazo": "2026-10-20",
            },
        )

        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(
            Tarefa.objects.filter(
                titulo="Estudar arquitetura MVC"
            ).exists()
        )

    def test_concluir_tarefa(self):
        tarefa = Tarefa.objects.create(
            titulo="Revisar conteúdo"
        )

        self.client.post(
            reverse("concluir_tarefa", args=[tarefa.id])
        )

        tarefa.refresh_from_db()
        self.assertTrue(tarefa.concluida)

    def test_excluir_tarefa(self):
        tarefa = Tarefa.objects.create(
            titulo="Tarefa para excluir"
        )

        self.client.post(
            reverse("excluir_tarefa", args=[tarefa.id])
        )

        self.assertFalse(
            Tarefa.objects.filter(id=tarefa.id).exists()
        )
