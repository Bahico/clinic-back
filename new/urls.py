from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewCreateView.as_view(), name='new-create'),
    path('<int:id>/', views.NewCreateView.as_view(), name='new-update-or-delete'),
    path('list/', views.NewView.as_view(), name='new-all'),
    path('detail/<int:id>/', views.NewView.as_view(), name='new-detail'),
]