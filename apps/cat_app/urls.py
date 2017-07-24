from django.conf.urls import url
from . import views

app_name = "cat"
urlpatterns = [
    url(r'^$', views.index, name="idx"),
    url(r'^add$', views.add, name="add"),
    url(r'^add/new$', views.addCat, name="ac"),
    url(r'^show/(?P<id>\w+)$', views.show, name="show"),
    url(r'^delete/(?P<id>\w+)$', views.delete, name="del"),
    url(r'^edit/(?P<id>\w+)$', views.edit, name="edit"),
    url(r'^update/(?P<id>\w+)$', views.update, name="update"),
    url(r'^like/(?P<id>\w+)$', views.like, name="like")
]
