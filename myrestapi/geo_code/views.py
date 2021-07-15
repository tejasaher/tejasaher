from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import geo_code
from .serializer import geo_codeSerializer

#from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#from rest_framework_simplejwt.authentication import JWTAuthentication 
# for JWT authentication_classes and that too when we need to use it on local level
#i.e for views. py otherwise direct add rest_framework_simplejwt.authentication.JWTAuthentication globally into settings

@api_view(['GET'])
#@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_geo_code(request):
	geo_info=geo_code.objects.all()
	serializer=geo_codeSerializer(geo_info,many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_geo_code(request):
	serializer = geo_codeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])

@permission_classes([IsAuthenticated])
def update_geo_code(request, pk):
	geo_record = geo_code.objects.get(seo_id=pk)
	print(geo_record)
	serializer = geo_codeSerializer(instance=geo_record, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_geo_code(request, pk):
	geo_record = geo_code.objects.get(seo_id=pk)
	geo_record.delete()

	return Response('Item succsesfully delete!')
