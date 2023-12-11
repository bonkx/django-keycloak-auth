from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


# @login_required
def index(request):
    # user = request.user
    return render(request, "web/home.html", {})


def pub(request):
    return render(request, "web/public.html", {})
