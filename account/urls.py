from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('buyer/', views.BuyerView.as_view()),
    path('buyer/<int:id>/', views.BuyerView.as_view()),
    path('', views.UserView.as_view()),
]
