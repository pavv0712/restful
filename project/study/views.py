from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer


# Create your views here.
@api_view(['GET'])
def StudentView(reuest):
    qs = Students.objects.all()
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ScoreView(reuest):
    qs = Scores.objects.all()
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data)