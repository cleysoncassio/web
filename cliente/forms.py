from django import forms

from .models import Cliente


class DateInput(forms.DateInput):
    input_type = "date"


class ClienteForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_legth": "Nome não pode ter mais de 30 caracteres"}
    )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_legth": "Sobrenome não pode ter mais de 30 caracteres"}
    )
    email = forms.EmailField(label="E-mail")
    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}",
        error_messages={"invalid": "Número de DDD inválido"}
    )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{9,15}",
        error_messages={"invalid": "Número de DDD inválido"},
    )

    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Cliente
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city",
        )
