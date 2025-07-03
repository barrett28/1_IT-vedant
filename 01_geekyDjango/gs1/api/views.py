from django.shortcuts import render
from . models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


def student_details(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

#  ------ jsonresponse
# def student_details(request, pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)  # jsonresponse use krte vakt is line ka kaam nhi hai
#     # return HttpResponse(json_data, content_type = 'application/json') # same iska bhi kaam nhi hai 
#     return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
    
    