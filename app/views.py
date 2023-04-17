from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print("In Home view")
    return HttpResponse("This is Home View....")

def greet(request):
    print("In Greet view")      
    return HttpResponse("This is Greet View....")

def exception_view(request):
    # print([1, 2, 3, 4][7])
    print(12/0)
    return HttpResponse("In exception_view.....")

def template_view(request):
    print("In template_view......")
    data = {"name": "Arun"}
    return TemplateResponse(request, template="index.html", context=data)