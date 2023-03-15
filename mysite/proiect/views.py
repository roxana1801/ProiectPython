from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from .models import Produse, Bakery


def index(request):
   return HttpResponse ("Hello, world. You're at the streaming app index.")

#def produse_list(request):
#   try:
#       produse=Produse.objects.all()
#   except Produse.DoesNotExist:
#       raise Http404(f"There is no shows in our DB!")
#  else:
#       return render(request, 'proiect/products.html', {"produse": produse})

class Produse_list(generic.ListView):
    model = Produse
    template_name = "proiect/products.html"
    context_object_name = "produse"

class ProductCreate(generic.CreateView):
    model = Produse
    template_name = "proiect/products_add.html"
    fields = ["denumire", "descriere", "ambalaj", "pret" , "id_poza"]
    context_object_name = "produse"
    success_url = reverse_lazy('about')

def Delete(DeleteView):
    model = Produse
    template_name = "proiect/products.html"
    context_object_name = "produse"
    success_url = reverse_lazy('products')

def home(request):
   #return HttpResponse ("mergeee aplicatiaaammmmmmmeeeaa")
   return render(request, 'proiect/home.html')

def about(request):
    #return HttpResponse("maboutttt")
    return render(request, 'proiect/about.html')

def store(request):
    #return HttpResponse("maboutttt")
    return render(request, 'proiect/store.html')

def productscoffe(request):
    return render(request, 'proiect/productscoffe.html')

#def bakery(request):
  #  return render(request, 'proiect/bakery.html')
def prezentareproduse(request):
    return render(request, 'proiect/prezentareproduse.html')

class Bakery(generic.ListView):
    model = Bakery
    template_name = "proiect/bakery.html"
    context_object_name = "bakery"







