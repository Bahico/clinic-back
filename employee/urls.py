from django.urls import path

from employee.views import EmployeeView, EmployeeHomeView

urlpatterns = [
    path('', EmployeeView.as_view()),
    path('home/', EmployeeHomeView.as_view()),
    path('<int:id>/', EmployeeView.as_view())
]
