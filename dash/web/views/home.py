from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from login_required import login_not_required


@login_not_required
def public(request):
    return render(request, "web/public.html", {})


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('oidc_authentication_init')
    # return render(request, "web/home.html", {})


def dashboard(request):
    return render(request, "web/dashboard.html", {})


def protected(request):
    return render(request, "web/protected.html", {})
