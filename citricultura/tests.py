import pytest
from rest_framework.test import APIClient

from .models import Produtor, Lote


@pytest.fixture
def produtor(db):
    return Produtor.objects.create(
        nome="João Silva", cidade="Olímpia", cpf_cnpj="123.456.789-00"
    )


def test_total_do_lote(produtor):
    lote = Lote.objects.create(
        produtor=produtor,
        variedade="Pera",
        caixas=10,
        preco_caixa=25,
        data="2026-11-23",
    )
    assert lote.total == 250


def test_filtro_por_variedade(client, produtor):
    Lote.objects.create(produtor=produtor, variedade="Pera", caixas=10, preco_caixa=25, data="2026-11-23")
    Lote.objects.create(produtor=produtor, variedade="Lima", caixas=5, preco_caixa=40, data="2026-11-23")

    resposta = client.get("/lotes/?variedade=Pera")

    assert resposta.status_code == 200
    lotes = list(resposta.context["lotes"])
    assert len(lotes) == 1
    assert lotes[0].variedade == "Pera"


def test_post_api_valido_retorna_201(produtor):
    api = APIClient()
    dados = {
        "produtor": produtor.id,
        "variedade": "Pera",
        "caixas": 8,
        "preco_caixa": "22.50",
        "data": "2026-11-23",
    }
    resposta = api.post("/api/lotes/", dados, format="json")
    assert resposta.status_code == 201


def test_post_api_invalido_retorna_400(produtor):
    api = APIClient()
    dados = {
        "produtor": produtor.id,
        "variedade": "Pera",
        "caixas": 0,
        "preco_caixa": "22.50",
        "data": "2026-11-23",
    }
    resposta = api.post("/api/lotes/", dados, format="json")
    assert resposta.status_code == 400