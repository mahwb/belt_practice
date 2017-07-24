# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from ..login_app.models import Users


class CatManager(models.Manager):
    def add(self, postData, request):
        passFlag = True
        if postData["name"] < 1 or not postData["name"]:
            messages.error(request, "Not valid name.")            
            passFlag = False
        if postData["age"] < 1 or not postData["age"] or not postData["age"].isdigit():
            messages.error(request, "Not valid age.")
            passFlag = False
        if passFlag == True:
            return Cat.objects.create(name=postData["name"], age=postData["age"], user=Users.objects.get(id=request.session["user_id"]))
        return False

    def update(self, postData, request, id):
        passFlag = True
        if postData["name"] < 1 or not postData["name"]:
            messages.error(request, "Not valid name.")            
            passFlag = False
        if postData["age"] < 1 or not postData["age"] or not postData["age"].isdigit():
            messages.error(request, "Not valid age.")
            passFlag = False
        if passFlag == True:
            cat = Cat.objects.get(id=id)
            if cat.user.id == request.session["user_id"]:
                cat.name = request.POST["name"]
                cat.age = request.POST["age"]
                cat.save()
                return cat
            else:
                messages.error(request, "Can't edit.")
        return False

class Cat(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default=0)
    user = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CatManager()

class Likes(models.Model):
    user = models.ForeignKey(Users, related_name="likes")
    cat = models.ForeignKey(Cat, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)