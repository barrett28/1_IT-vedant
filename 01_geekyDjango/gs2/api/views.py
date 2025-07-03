from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import io
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'}) 
        return JsonResponse(serializer.errors, status=400) 
