from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='primulapi'),
    path('produse/', views.Produse_list.as_view(), name='products'),
    path('produse/products_add', views.ProductCreate.as_view(), name='products_add'),
    path('produse/delete/<int:pk>', views.produs_delete.as_view(), name='confirm_delete'),
    path('produse/home', views.home, name='home'),
    path('produse/about', views.about, name='about'),
    path('produse/store', views.store, name='store'),
    path('produse/productscoffe', views.productscoffe, name='productscoffe'),
    path('produse/bakery', views.Bakery.as_view(), name='bakery'),
    path('produse/prezentareproduse', views.prezentareproduse, name='prezentareproduse' )
]