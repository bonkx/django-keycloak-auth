from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def public(request):
    return render(request, "web/public.html", {})


@login_required
def index(request):
    # user = request.user
    return render(request, "web/home.html", {})


@login_required
def protected(request):
    return render(request, "web/protect.html", {})
