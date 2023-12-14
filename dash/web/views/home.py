from django.shortcuts import render

# Create your views here.


def public(request):
    return render(request, "web/public.html", {})


def index(request):
    # user = request.user
    return render(request, "web/home.html", {})


def protected(request):
    return render(request, "web/protect.html", {})
