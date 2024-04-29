from django.urls import path

from . import views


urlpatterns = [
    path("home/", views.home,name="home"),
    path("weatherinfo/", views.weatherinfo, name="weatherinfo"),
    path("contactmail/",views.contactmail , name = "contactmail"),
    path("",views.login,name="login"),
    path("SignUp",views.Signup,name="SignUp"),

]