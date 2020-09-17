from django.shortcuts import render
from .serializers import Signup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model

# Create your views here.
@api_view(['GET', 'POST'])
def signup(request):

    
    if request.method == 'GET':
        users = Signup(data = User.objects.all())
        return Response(users)

    
    
    elif request.method == 'POST':
        signup = Signup(data = request.data)
        if signup.is_valid():
            signup.save()
            return Response

    