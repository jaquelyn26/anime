from django.shortcuts import render

# Create your views here.
def Mascotas(request):
    return render(request, 'index.html')

def anime(request):
    return render(request, 'furnitures.html')

def chormi(request):
    return render(request, 'about.html')

def jaq(request):
    return render(request, 'contact.html')

def samm(request):
    return render(request, 'company.html')