from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path("base",views.welcome, name="base"),
    path("aboutme",views.aboutme_fun, name="aboutme"),
    path("contactus",views.contactus_fun, name="contactus"),
    path("chatBot",views.user_input, name="chatBot"),
    path("signup",views.signup_view, name="signup"),
    path("",views.login_view, name="login"),
    path("logout",views.logout_fun, name="logout"),

]
