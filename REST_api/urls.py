from django.urls import path
from . import views

urlpatterns = [
    path('branches/autocomplete',views.autoComplete,name=""),
    path('branches/search',views.search,name=""),
    path("",views.empty,name=""),
]
