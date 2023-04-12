from django.urls import path

from .views import ProductView, ProductListView

urlpatterns = [
    path('', ProductView.as_view()),
    path('edit/<int:id>/', ProductView.as_view()),
    path('list/', ProductListView.as_view())
]
