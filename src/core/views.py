from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomLoginForm
from ..consumer.models import User
from django.contrib.auth import get_user_model


def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "index.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                get_user_model().objects.create(
                    user_user=user
                )
                return redirect(
                    "src.core:login_view"
                )
            except Exception as e:
                print(f"Erro ao criar User: {e}")  # TODO Print

    else:
        form = CustomUserCreationForm()

    return render(request, "user/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("establishment:dashboard")
    else:
        form = CustomLoginForm()

    return render(request, "user/login.html", {"form": form})