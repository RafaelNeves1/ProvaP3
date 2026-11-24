from django import forms
from .models import Lote


class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ["produtor", "variedade", "caixas", "preco_caixa", "data"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_caixas(self):
        caixas = self.cleaned_data["caixas"]
        if caixas < 1:
            raise forms.ValidationError("O lote deve ter pelo menos 1 caixa.")
        return caixas