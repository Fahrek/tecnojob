from django.urls import path
from .views import ViewRegister, access, salir


urlpatterns = [
    path('registrar/', ViewRegister.as_view(), name="registro"),
    path('acceder/', access, name="acceder"),
    path('salir/', salir, name="salir"),
]
