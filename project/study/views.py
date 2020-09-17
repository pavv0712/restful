from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer, StudentBasicSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import StudentBasicSerializer, ScoresBasicSerializer, StudentSerializer, ScoreSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def StudentBasicView(request):
    if request.method == 'GET':
        student = Students.objects.all()
        serializer = StudentBasicSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentBasicSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def StudentDetailBasicView(request, pk):
    if request.method == 'PUT':
        student = Students.objects.get(pk=pk)
        #student 원래데이터
        #request.data 사람이 보내준 데이터
        #(원래데이터 <- 사람이 보내준 데이터) -> SAVE 
        serializer = StudentBasicSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)




class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs

    @action(detail=False, methods=['GET'])
    def suwon(self, request):
        qs = self.get_queryset().filter(address_contains='수원')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def init(self, request, pk):
        instance = self.get_object()
        instance.address = ""
        instance.email = ""
        instance.save(update_fields=['adderss', 'email'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

@api_view(['GET','POST'])
def ScoreBasicView(request):
    if request.method == 'GET':
        scores = Scores.objects.all()
        print('1')
        serializer = ScoresBasicSerializer(scores, many=True)
        print('2')
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScoresBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ScoreView(viewsets.ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoreSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name')
        math = self.request.query_params.get('math')
        english = self.request.query_params.get('english')
        science = self.request.query_params.get('science')
        order = self.request.query_params.get('order')

        if name:
            qs = qs.filter(name=name)
        if math:
            qs = qs.filter(math__gt=math)
        if english:
            qs = qs.filter(english__gt=english)
        if science:
            qs = qs.filter(science__gt=science)
        if order:
            qs = qs.order_by(order)
        return qs
    
        @action(detail=False, methods=['GET'])
        def top(self, request):
            qs = self.get_queryset().filter(math__gte=20, english_gte=30, science_gte=40 )
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data)



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

