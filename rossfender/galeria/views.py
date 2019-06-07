from django.shortcuts import render
from .models import Gallery

# Create your views here.
def portafolio(request):
    #variable para guardar la lista de pasteles
    cakesList =  Gallery.objects.all()
    return render(request,'galeria/portafolio.html',{'cakes':cakesList})