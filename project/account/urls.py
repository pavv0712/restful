from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signup),
    path('api-jwt-auth/', obtain_jwt_token),
    path('refresh_jwt_token/', refresh_jwt_token),
    path('verify_jwt_token/', verify_jwt_token)
]