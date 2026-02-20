from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print("request is: ",request)
    return HttpResponse("Hello, World! This is Abhishek Roka's Website")

