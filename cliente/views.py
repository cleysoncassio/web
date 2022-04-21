# from django.shortcuts import render

from django.views.generic import ListView, CreateView
from .models import Cliente
from .forms import ClienteForm


class ClienteListView(ListView):
    template_name = "cliente/cliente_list.html"
    model = Cliente
    queryset = Cliente.objects.all()


class ClienteCreateView(CreateView):
    template_name = "cliente/cliente.html"
    form_class = ClienteForm

    def form_valid(self, form):
        return super().form_valid(form)

# def novo(request):
# return render(request, 'cliente/novo.html')
