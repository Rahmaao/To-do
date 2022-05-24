from django.urls import path
from . import views


urlpatterns = []


urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.category, name="categories"),
    path("categories/<int:pk>/delete/", views.deletecategory, name="deletecategory"),
    path("categories/<int:pk>/update/", views.updatecategory, name="updatecategory"),
    path("todo/<int:pk>", views.todo, name="todo"),
    path("deletetodo/<int:pk>", views.deletetodo, name="deletetodo"),
    path("updatetodo/<int:pk>", views.updatetodo, name="updatetodo"),
    path("item/<int:pk>", views.item, name="item"),
    path("deleteitem/<int:pk>", views.deleteitem, name="deleteitem"),
    path("updateitem/<int:pk>", views.updateitem, name="updateitem"),
    path("complete/<int:pk>", views.complete, name="completeitem"),
]
