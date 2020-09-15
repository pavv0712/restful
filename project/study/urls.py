from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('students', views.StudentView)
# router.register('scores', views.ScoreView)

urlpatterns = [
    # path('students', include(router.urls)),
    # path('scores', include(router.urls))
    # path('students', views.StudentView.as_view())
    
    path('students/', views.StudentView),
    path('scores/', views.ScoreView),
    path('students/<id>', views.StudentDetailView),
    path('scores/<id>', views.ScoreDetailView)

]