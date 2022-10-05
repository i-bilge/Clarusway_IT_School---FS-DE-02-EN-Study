from django.urls import path
from .views import StudentDUD, StudentList, StudentListCreateAPI, StudentListGeneric, home, StudentDetailUpdateDelete

urlpatterns = [
    path('', StudentList.as_view()),
    path('<int:pk>/', StudentDetailUpdateDelete.as_view()),
    path('list1', StudentListGeneric.as_view()),
    path('list2', StudentListCreateAPI.as_view()),
    path('dud/<int:pk>/', StudentDUD.as_view()),
]