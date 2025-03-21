from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def get_student(request, id=None):
    return Response(StudentSerializer(get_object_or_404(Student, id=id) if id else Student.objects.all(), many=not id).data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    return Response({'msg': 'Student Created'} if serializer.is_valid() and serializer.save() else serializer.errors)

@api_view(['PUT'])
def update_student(request, id):
    serializer = StudentSerializer(get_object_or_404(Student, id=id), data=request.data, partial=True)
    return Response({'msg': 'Student Updated'} if serializer.is_valid() and serializer.save() else serializer.errors)

@api_view(['DELETE'])
def delete_student(request, id):
    get_object_or_404(Student, id=id).delete()
    return Response({'msg': 'Student Deleted'})
# Create your views here.
