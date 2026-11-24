from django.core.validators import MinValueValidator
from django.db import models

VARIEDADE_CHOICES = [
    ("Pera", "Pera"),
    ("Valência", "Valência"),
    ("Lima", "Lima"),
]


class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome


class Lote(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    variedade = models.CharField(max_length=20, choices=VARIEDADE_CHOICES)
    caixas = models.IntegerField(validators=[MinValueValidator(1)])
    preco_caixa = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data = models.DateField()

    @property
    def total(self):
        return self.caixas * self.preco_caixa