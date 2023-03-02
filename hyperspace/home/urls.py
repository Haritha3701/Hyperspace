from django.urls import path
from . import views

urlpatterns = [
    path("",views.samp),
    path('login/',views.login,name="loginpage"),
    path('register/',views.register,name="regpage"),
    path('logout/',views.logout)
]