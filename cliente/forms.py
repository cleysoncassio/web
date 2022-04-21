from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField()
    area_code = forms.CharField()
    phone_number = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

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
