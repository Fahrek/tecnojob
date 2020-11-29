from django.urls import path
from .views import index, offer_insert, offer_select


urlpatterns = [
    path('', index, name='buscador'),
    path('crear/', offer_insert, name="crear"),
    path('mostrar/', offer_select, name="mostrar"),
]
