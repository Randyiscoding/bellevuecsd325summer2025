from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Easton says Hello!")
# Create your views here.
