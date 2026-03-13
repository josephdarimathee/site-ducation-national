from django.shortcuts import render

def accuiel(request):
    return render(request, 'siteweb/accuiel.html')

def about(request):
    return render(request, 'siteweb/about.html')

def contact(request):
    return render(request, 'siteweb/contact.html')

def actualite(request):
    return render(request, 'siteweb/actualite.html')

def academique(request):
    return render(request, 'siteweb/academique.html')

def campus(request):
    return render(request, 'siteweb/campus.html')
# Create your views here.
