from django.urls import path
from . import views

urlpatterns = [
    path('branches/autocomplete',views.autoComplete,name=""),
    path("",views.empty,name=""),
]
