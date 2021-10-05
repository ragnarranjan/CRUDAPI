from django.shortcuts import render
from rest_framework.views import APIView
from crud.models import Bio
from rest_framework.response import Response
from crud.serializers import BioSerializers
from rest_framework import status
from django import http


class Bioview(APIView):
    def get(self,request):
        bio = Bio.objects.all()
        serializer = BioSerializers(bio,many = True)
        return Response(serializer.data)
        

    def post(self,request):
        serializer = BioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BioDetailview(APIView):
    def get_detail(self,pk):
        try:
            return Bio.objects.get(pk=pk)
        except Bio.DoesNotExist:
            raise HTTP_404_NOT_FOUND
        
    def get(self,request,pk):
        biodetail = self.get_detail(pk)
        serializers = BioSerializers(biodetail)
        return Response(serializers.data,status = status.HTTP_200_OK)


    def put(self,request,pk):
        biodetail = self.get_detail(pk)
        serializer = BioSerializers(biodetail,data = request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            print("-----------inside serializer----", serializer.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(request,pk):
        biodetail = self.get_detail(pk)
        biodetail.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
            

