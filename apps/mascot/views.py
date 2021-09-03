from django.shortcuts import render

# Create your views here.
def Mascotas(request):
    return render(request, 'index.html')

def anime(request):
    return render(request, 'segunda_pag.html')