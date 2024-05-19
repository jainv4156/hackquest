from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import complainRequest
from .serializer import complainserializer
import json
from datetime import datetime

# Create your views here.
@api_view(['POST'])
def createComplain(request):
    if request.method == 'POST':
        complaindata = json.loads(request.data['complaindata'])
        serializer = complainserializer(data=complaindata)
        if( complaindata["name"]==None or complaindata["name"]==''):

            complaindata["name"]='Anonymous'
        
        complain=complainRequest(victim=complaindata["victim"],discrption=complaindata["discription"],address=complaindata["address"],date=datetime.today(),time=datetime.now(),status='Pending',name=complaindata["name"],phone=complaindata["phone"],email=complaindata["email"])
        print("Complain created successfully")
        complain.save()
        return Response({'message':'Complain created successfully',"id":complain.id})
@api_view(['POST'])
def getComplain(request):
    if request.method == 'POST':
        id=request.data
        print(id)
        complains = complainRequest.objects.all().filter(id=id)
        serializer = complainserializer(complains, many=True)
        return Response(serializer.data)