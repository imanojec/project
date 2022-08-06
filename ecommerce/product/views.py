from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from product.models import Login
from product.serializers import LoginSerializer


@csrf_exempt
def loginApi(request,id=0):
    if request.method=='GET':
        login=Login.objects.all()
       
        login_serializer=LoginSerializer(login,many=True)
        return JsonResponse(login_serializer.data,safe=False)
    
    elif request.method=='POST':
        login_data=JSONParser().parse(request)
        login_serializer=LoginSerializer(data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    
    elif request.method=='PUT':
        login_data=JSONParser().parse(request)
        login=Login.objects.get(UserId=login_data['UserId'])
        login_serializer=LoginSerializer(login,data=login_data)
        if login_serializer.is_valid():

            login_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("failed to update")
    
    elif request.method=='DELETE':
        login=Login.objects.get(UserId=id)
        login.delete()
        return JsonResponse("deleted successfully",safe=False)

