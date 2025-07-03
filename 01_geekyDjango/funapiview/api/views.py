from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import StudentSerializer
# Create your views here.

''' browser api k sath kama krne k liye (pk = None) likhna padega and
 id = request.data.get('id') ki jagha hm (id = pk) likh sakte hai ye changes (post, put, patch, delete) me honge
'''

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many= True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'added successfully'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"updated successfully"}
            return Response(res)
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg":"deleted successfully"}
        return Response(res)
    return Response("something went wrong")