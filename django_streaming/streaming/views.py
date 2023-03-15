from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, Http404

from .models import Show


# APIs
def index(request):
    return HttpResponse("Hello, world. You're at the streaming app index.")


# GET ALL SHOWS
# def show_list(request):
#     # luam toate show-urile din db
#     # trimitem lista de show-uri catre template
#     # incarcam template-ul
    
#     try:
#         shows = Show.objects.all()
#     except Show.DoesNotExist:
#         raise Http404(f"There is no shows in our DB!")
#     else:
#         return render(request, 'streaming/show_list.html', {"shows": shows})

# view-ul de GET ALL SHOWS de mai sus scris cu ajutorul generic class view ListView 
class ShowList(generic.ListView):
    model = Show
    template_name = "streaming/show_list.html"
    context_object_name = "shows"



# GET SHOW BY ID
class ShowDetails(generic.DetailView):
    model = Show
    template_name = "streaming/show_details.html"
    context_object_name = "show"


# DELETE SHOW
class ShowDelete(generic.DeleteView):
    model = Show
    template_name = "streaming/confirm_delete.html"
    context_object_name = "show"
    success_url = reverse_lazy('show_list')

# ADD SHOW
class ShowCreate(generic.CreateView):
    model = Show
    template_name = "streaming/show_form.html"
    fields = ["title", "type", "subtitle_languages", "length_minutes" , "nr_of_episodes", "poster"]
    context_object_name = "show"
    success_url = reverse_lazy('show_list')
    # API-uri care presupun form-uri pot primi un atribut form_class = ShowForm 
    # clasa ShowForm trebuie sa mosteneasca de la clasa django.forms.Form sau ModelForm 4
    # si care poate adauga functionalitati specifice fiecarui field al formului
    # cum ar fi label cu text descriptiv, widget special diferit de cel default, validare extra, etc. 

# UPDATE SHOW
class ShowUpdate(generic.UpdateView):
    model = Show
    template_name = "streaming/show_form.html"
    fields = ["title", "type", "subtitle_languages", "length_minutes" , "nr_of_episodes", "poster"]
    context_object_name = "show"
    success_url = reverse_lazy('show_list')



# DISPLAY series / movies
class ShowListFilteredByType(generic.ListView):
    model = Show
    template_name = "streaming/show_list.html"
    context_object_name = "shows"

    def get_queryset(self):
        return Show.objects.filter(type=self.kwargs['show_type'])  # "SELECT * FROM Show WHERE type=?" unde ? = movie/tv_series


# TODO: api de ADD TO FAVORITES care presupune modificarea unui camp in baza de date is_favorite = True


# TODO: USER APIs 


# DEZVOLTARI ULTERIOARE:
# 1. de adaugat APIs de CRUD pentru User (cu template-uril aferente)
# 2. de adagaugat APIs pentru Provider (+ templates)
# 3. de cautat pe net cum se face o legatura many-to-many intre Show si Provider 
# hint: la clasa Show trebuie adaugat field-ul: providers = models.ManyToManyField(Provider)
# 4. adaugare functionalitate de login/logout
# 5. pagina listare show-uri doar de la un anumite provider (de ex: doar filme si seriale de pe Netflix) 
# 6. pagina listare show-uri de un anumite tip de la un anumit provider (de ex: doar seriale de pe Netflix)
# ...limita e doar imaginatia voastra :)