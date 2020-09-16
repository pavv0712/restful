from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentView)
router.register('scores', views.ScoreView)

urlpatterns = [

    path('', include(router.urls)),
    path('test', views.StudentBasicView),
    path('test/<pk>', views.StudentDetailBasicView),
    path('testscore', views.ScoreBasicView)
    
    # path('students/', views.StudentView),
    # path('scores/', views.ScoreView),
    # path('students/<id>', views.StudentDetailView),
    # path('scores/<id>', views.ScoreDetailView)

]