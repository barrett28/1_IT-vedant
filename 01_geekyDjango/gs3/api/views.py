from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)  # ✅ missing part
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data posted successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer=  StudentSerializer(stu, data = pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg' : 'data deleted successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = "application/json")
        
        