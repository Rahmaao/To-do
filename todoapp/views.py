from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models

# Create your views here.


# function to add and display the categories in the db


def index(request):
    return render(request, "home.html")


def category(request):
    if request.method == "POST":
        addcategory = request.POST["name"]  # categories from html
        models.Category.objects.create(
            name=addcategory
        )  # first part is model field name while the second part is the one in the view function variable you created above
    categories = models.Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories.html", context)


# function to delete each category in db


def deletecategory(request, pk):
    deletecategory = models.Category.objects.get(pk=pk)
    deletecategory.delete()
    return redirect(
        reverse("index")
    )  # redirect to the original page (which is named in the urls.py) after deleting


# function to update each category


def updatecategory(request, pk):
    if request.method == "POST":
        categoryname = request.POST["categoryname"]
        updatecategory = models.Category.objects.get(pk=pk)
        updatecategory.name = categoryname  # the item you have gotten .model field will be changed to what was given in th epost request
        updatecategory.save()
        return redirect(
            reverse("index")
        )  # name of url to redirect to after updating is complete
    return render(
        request, "update.html"
    )  # the original template that will be shown once an update operation is initiated


# function to add and display every todo in db


def todo(request, pk):
    if request.method == "POST":
        addtodo = request.POST[
            "addtodo"
        ]  # new var is equal to the post request as the var is saved in the html
        thiscategory = models.Category.objects.get(
            pk=pk
        )  # set new todo in particular category where pk is equal to the current pk (pk of the category)
        models.Todo.objects.create(
            name=addtodo, category=thiscategory
        )  # the model field is equal to the variables in the view function above
    todocategory = get_object_or_404(models.Category, pk=pk)
    todolist = models.Todo.objects.filter(
        category=todocategory
    )  # filter using the fk in the model , category, i guess
    context = {"todocategory": todocategory, "todolist": todolist}
    return render(request, "todo.html", context)


# function to delete each todo in db


def deletetodo(request, pk):
    deletethistodo = models.Todo.objects.get(pk=pk)
    deletethistodo.delete()
    return redirect(reverse("todo", kwargs={"pk": deletethistodo.category.pk}))


# function to update each todo in db


def updatetodo(request, pk):
    if request.method == "POST":
        todoname = request.POST["modifytodo"]
        updatetodo = models.Category.objects.get(pk=pk)
        updatetodo.name = todoname
        updatetodo.save()
        return redirect(reverse("todo", kwargs={"pk": updatetodo.category.pk}))
    return render(request, "updatetodo.html")


# function to add and display every item in each todo


def item(request, pk):
    if request.method == "POST":
        additem = request.POST[
            "additem"
        ]  # new var is equal to the post request as the var is saved in the html
        thistodo = models.Todo.objects.get(
            pk=pk
        )  # set new todo in particular category where pk is equal to the current pk (pk of the category)
        models.Item.objects.create(
            description=additem, todo=thistodo
        )  # the model field is equal to the variables in the view function above
    todolist = get_object_or_404(models.Todo, pk=pk)
    todoitem = models.Item.objects.filter(
        todo=todolist
    )  # filter using the fk in the model , todo, i guess
    context = {"todolist": todolist, "todoitem": todoitem}
    return render(request, "items.html", context)


# function to delete each item in todo


def deleteitem(request, pk):
    deletethisitem = models.Item.objects.get(pk=pk)
    deletethisitem.delete()
    return redirect(reverse("item", kwargs={"pk": deletethisitem.todo.pk}))


# function to update each item in todo


def updateitem(request, pk):
    if request.method == "POST":
        itemname = request.POST["modifyitem"]
        updateitem = models.Todo.objects.get(pk=pk)
        updateitem.description = (
            itemname  # .modelfield you want to update = the post request variable
        )
        updateitem.save()
        return redirect(reverse("item", kwargs={"pk": updateitem.todo.pk}))
    return render(request, "updateitem.html")


# function to complete items


def complete(request, pk):
    thisitem = models.Item.objects.get(pk=pk)
    thisitem.completed = not thisitem.completed
    thisitem.save()
    return redirect(reverse("item", kwargs={"pk": thisitem.todo.pk}))
