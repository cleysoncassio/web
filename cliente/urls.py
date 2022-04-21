from django.urls import path

#from cliente.views import novo

from .views import ClienteListView, ClienteCreateView


app_name = "cliente"

urlpatterns = [
    path('list/', ClienteListView.as_view(), name="cliente_list"),
    path('', ClienteCreateView.as_view(), name="cliente-create"),
]

