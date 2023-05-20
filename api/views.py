from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Model Object - Single Student Data

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data)

# Query Set - All Student Data
def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu, many=True)
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def student_create(request):
 if request.method == 'POST':
    json_data = request.body
    #   print(json_data,'yyyyyyy')
    stream = io.BytesIO(json_data)
    #   print(stream,'xxxxxxxxxx')
    pythondata = JSONParser().parse(stream)
    #   print(pythondata,'zzzzzzzz')
    serializer = StudentSerializer(data=pythondata)
    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data Created Successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def student_put(request,pk):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        #  Complete Update - Required All Data from Front End/Client
        #  serializer = StudentSerializer(stu, data=pythondata) 
        #  Partial Update - All Data not required
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated Successfully !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def student_delete(request,pk):  
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted Successfully!!'}
        # json_data = JSONRenderer().render(res)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(res, safe=False)
