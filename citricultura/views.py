from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Lote
from .forms import LoteForm
from .serializers import LoteSerializer


def lote_list(request):
    # Tarefa 3: lista os lotes e envia ao template
    lotes = Lote.objects.select_related("produtor").all()

    # Tarefa 4: filtro por variedade lido da URL (?variedade=...)
    variedade = request.GET.get("variedade")
    if variedade:
        lotes = lotes.filter(variedade=variedade)

    return render(request, "citricultura/lista.html", {
        "lotes": lotes,
        "variedade_atual": variedade,
    })


def lote_detail(request, id):
    # Tarefa 6: detalhe com get_object_or_404
    lote = get_object_or_404(Lote.objects.select_related("produtor"), id=id)
    return render(request, "citricultura/detalhe.html", {"lote": lote})


def lote_create(request):
    if request.method == "POST":
        form = LoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lote_list")
    else:
        form = LoteForm()
    return render(request, "citricultura/form.html", {"form": form})


class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.select_related("produtor").all()
    serializer_class = LoteSerializer
    