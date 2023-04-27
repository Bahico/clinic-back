from django.urls import path

from . import views

urlpatterns = [
    path('', views.PartnerView.as_view()),
    path('<int:id>/', views.PartnerView.as_view()),
    path('create/', views.PartnerCreateView.as_view()),
    path('update/<int:id>/', views.PartnerCreateView.as_view()),
]