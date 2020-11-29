from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def access(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenid@ de nuevo {username}")
                return redirect("buscador")
            else:
                messages.success(request, "Los datos son incorrectos")
        else:
            messages.success(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, "access.html", {"form": form})


# Create your views here.
class ViewRegister(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Bienvenid@ a la plataforma {username}")
            login(request, user)
            return redirect("buscador")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "register.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, f"Tu sesión se ha cerrado correctamente")
    return redirect("acceder")
