from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('shows/', views.show_list, name='show_list'),
    path('shows/', views.ShowList.as_view(), name='show_list'),    
    path('shows/<int:pk>', views.ShowDetails.as_view(), name='show_details'),
    path('shows/delete/<int:pk>', views.ShowDelete.as_view(), name='show_delete'),
    path('shows/add', views.ShowCreate.as_view(), name='show_create'),
    path('shows/update/<int:pk>', views.ShowUpdate.as_view(), name='show_update'),
    path('shows/<str:show_type>', views.ShowListFilteredByType.as_view(), name='show_list_by_type'),
]