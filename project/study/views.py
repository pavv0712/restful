from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework import status, viewsets
from rest_framework.views import APIView


# Create your views here.

# class StudentView(viewsets.ModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

#     def get_queryset(self):
#         qs = super().get_queryset()

#         name = self.request.query_params.get('name')
#         if name:
#             qs = qs.filter(name=name)
#         return qs

#     @action(detail=False, methods=['GET'])
#     def suwon(self, request):
#         qs = self.get_queryset().filter(address_contains='수원')
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     @action(detail=True, methods=['PUT'])
#     def init(self, request, pk):
#         instance = self.get_object()
#         instance.address = ""
#         instance.email = ""
#         instance.save(update_fields=['adderss', 'email'])
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)







# class StudentView(APIView):
#     def get(self, request):
#         qs = Students.objects.filter()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'POST'])

# def StudentView(request):
#     #조회
#     if request.method == 'GET':
#         qs = Students.objects.filter()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
#     #입력
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def StudentDetailView(request, id):
#     #상세조회
#     qs = Students.objects.get(pk=id)
#     if request.method == 'GET': 
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
#     #수정
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(qs, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
#     #삭제
#     elif request.method == 'DELETE':
#         qs.delete()
#         return Response(status=204)

# @api_view(['GET', 'POST'])
# def ScoreView(request):
#     if request == 'GET':
#         scores = Scores.objects.all()
#         serializer = ScoreSerializer(scores, many=True)
#         return Response(serializer.data)
      #추가
#     elif request == 'POST':
#          serializer = ScoreSerializer(data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data, status = status.HTTP_201_CREATED)
#          return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

# @api_view(['GET', 'PUT', 'DELETE'])

# def ScoreDetailView(request, id):
#     scores = get_object_or_404(Scores, pk = id)

#     if request == 'GET':
#         serializer = ScoreSerializer(scores)
#         return Response(serializer.data)
#     elif request == 'PUT':
#         serializer = ScoreSerializer(scores, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
#     elif request == 'DELETE':
#         scores.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

