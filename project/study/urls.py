from . import views
from django.urls import path, include

urlpatterns = [
    path('students/', views.StudentView),
    path('scores/', views.ScoreView)

]