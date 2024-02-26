from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import * 
# Create your views here.


class HandleFileUpload(APIView);
    def post(self,request):
        try:
            data = request.data
            serializer = FileListSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status" : 200,
                    "message": "File Uploaded",
                })
            return Response({
                "status": 400,
                "message": "something went wrong",
                "data": serializer.errors
            })
        except Exception as e:
            print(e)

