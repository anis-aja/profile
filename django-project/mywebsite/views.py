from django.http import HttpResponse
from django.shortcuts import render

def indexa(request):
    return HttpResponse("Hallo saya disini")

def indexb(request):
    return render(request, 'index.html')

