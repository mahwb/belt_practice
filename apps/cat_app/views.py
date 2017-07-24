# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cat, Likes, Users
from django.shortcuts import render, redirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.contrib import messages


# shows main page
def index(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    data = {
        "cats": Cat.objects.all().annotate(count=Count("likes"))
    }
    return render(request, "cat_app/index.html", data)

# shows add cat page
def add(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    return render(request, "cat_app/add.html")

# shows cat info
def show(request, id):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    data = {
        "cat": Cat.objects.get(id=id)
    }
    return render(request, "cat_app/show.html", data)

# shows edit page
def edit(request, id):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    data = {
        "cat": Cat.objects.get(id=id)
    }
    return render(request, "cat_app/edit.html", data)

# updates the cat info
def update(request, id):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    cat = Cat.objects.update(request.POST, request, id)
    if cat == False:
        return redirect(reverse("cat:edit", kwargs={'id': id }))
    return redirect("cat:idx")

# deletes cat entry
def delete(request, id):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    Cat.objects.get(id=id).delete()
    return redirect("cat:idx")

# adds cat
def addCat(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    cat = Cat.objects.add(request.POST, request)
    if cat == False:
        return redirect("cat:add")
    return redirect("cat:idx")

# adds a like
def like(request, id):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    Likes.objects.create(user=Users.objects.get(id=request.session["user_id"]), cat=Cat.objects.get(id=id))
    return redirect("cat:idx")