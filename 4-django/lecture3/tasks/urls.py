from django.urls import path 

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    # "add" route, views.add - add function, name="add"
    path("add", views.add, name="add")
]