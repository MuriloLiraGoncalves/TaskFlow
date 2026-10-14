from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm


def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by("-id")
    formulario = TarefaForm()

    if request.method == "POST":
        formulario = TarefaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_tarefas")

    return render(
        request,
        "tarefas/lista.html",
        {
            "tarefas": tarefas,
            "formulario": formulario,
        },
    )


def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect("lista_tarefas")


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect("lista_tarefas")