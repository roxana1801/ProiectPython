from django.shortcuts import render, redirect
from .models import Produse, Bakery
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView
from django.http import HttpResponse, Http404


def index(request):
   return render(request, 'proiect/home.html')

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
    fields = ["denumire", "descriere", "ambalaj", "id_poza"]
    context_object_name = "produse"
    success_url = reverse_lazy("products")

#class ProduseUpdate(generic.UpdateView):
#    model = Produse
#    template_name = "proiect/products_add.html"
#    fields = ["denumire", "descriere", "ambalaj", "pret", "id_poza"]
#    context_object_name = "produse"
#    success_url = reverse_lazy('prezentareproduse')

class produs_delete(generic.DeleteView):
    model = Produse
    template_name = "proiect/confirm_delete.html"
    context_object_name = "produse"
    success_url = reverse_lazy("products")

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







