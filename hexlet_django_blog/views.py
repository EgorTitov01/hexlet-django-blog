from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


def index(request):
    return render(
        request,
        "index.html",
    )

def about(request):
    return render(request, "about.html")

