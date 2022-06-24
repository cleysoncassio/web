# from django.shortcuts import render

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q


class ClienteListView(ListView):
    template_name = "cliente/cliente_list.html"
    paginate_by = 4
    model = Cliente

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class ClienteCreateView(CreateView):
    template_name = "cliente/cliente.html"
    form_class = ClienteForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cliente:cliente_list")


class ClienteUpdateView(UpdateView):
    template_name = "cliente/cliente.html"
    form_class = ClienteForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Cliente, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cliente:cliente_list")


class ClienteDeleteView(DeleteView):

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Cliente, id=id)

    def get_success_url(self):
        return reverse("cliente:cliente_list")
