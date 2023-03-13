
from django.urls import path
from . import views

urlpatterns = [
    path("",views.details),
    path("cmt/",views.commentsub,name="commentbox"),

]