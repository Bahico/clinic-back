from django.urls import path

from .views import ProductView, ProductListView, VideoView

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:id>/', ProductView.as_view()),
    path('edit/<int:id>/', ProductView.as_view()),
    path('list/', ProductListView.as_view()),
    path('video/', VideoView.as_view()),
    path('video/<int:id>/', VideoView.as_view())
]
