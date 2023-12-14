from django.shortcuts import render
from login_required import login_not_required

# Create your views here.


@login_not_required
def public(request):
    return render(request, "web/public.html", {})


def index(request):
    # user = request.user
    return render(request, "web/home.html", {})


def protected(request):
    return render(request, "web/protect.html", {})
