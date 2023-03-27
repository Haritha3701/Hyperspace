from django.urls import path
from . import views
from .feed import latestplan

urlpatterns = [
    path("",views.samp,name="homepage"),
    path('login/',views.login,name="loginpage"),
    path('register/',views.register,name="regpage"),
    path('logout/',views.logout),
    path('feed/',latestplan())
]