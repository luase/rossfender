from django.shortcuts import render,HttpResponse
html_base = """

"""
# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def portafolio(request):
    return render(request,"core/portafolio.html")

def contacto(request):
    return render(request,"core/contacto.html")