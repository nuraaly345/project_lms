from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'mainapp/home.html')
    #return HttpResponse("Hello world")