from django.urls import path
from . import views

urlpatterns = [
    path('',views.account.as_view()),
    path('login',views.login.as_view()),  
]