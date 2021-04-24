from django.urls import path
from . import views
from .views import *

app_name="accounts"

urlpatterns = [
	path('signup/', views.signup, name="signup"),
	path('signin/', views.signin, name="signin"),
	path('logout/', views.signout, name="logout"),

]
