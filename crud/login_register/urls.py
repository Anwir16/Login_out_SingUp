from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name="Home"),
    path('signup/',views.signup, name="Signup"),
    path('logout/',views.logoutViews, name="logout"),
    path('login/',views.loginViews, name="login"),
]