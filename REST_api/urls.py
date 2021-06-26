from django.urls import path
from . import views

urlpatterns = [
    path('branches/autocomplete',views.autoComplete,name=""),
    path('branches',views.search,name=""),
    path('setFav',views.Fav,name=""),
    path("",views.empty,name=""),
]
