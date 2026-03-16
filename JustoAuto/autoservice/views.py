from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Labas, pasauli!")

from django.shortcuts import render

def index(request):
    return render(request, template_name="index.html")