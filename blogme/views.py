from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("BlogMe!")


def custom404(request, exception):
    return render(request, "pages/404.html")
