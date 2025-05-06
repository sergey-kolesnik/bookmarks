from django.contrib.auth import authenticate, login
from django.http import (
    HttpResponse, 
    HttpRequest,
)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd["username"],
                password = cd["password"],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated sus=ccessfully")
                else:
                    return HttpResponse("Disabled account", status=403)
            else:
                return HttpResponse("invalid login", status=401)
    else:
        form = LoginForm()
        return render(
            request,
            "account/login.html",
            {
                "form": form
            }
        )


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "account/dashboard.html",
        {
            "section": "dashboard"
        }
    )
