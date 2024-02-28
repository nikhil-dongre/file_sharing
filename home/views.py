from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import * 
import pdb
import status
# Create your views here.
def home(request):
    return render(request, 'home.html')

class HandleFileUpload(APIView):
    print("Inside handle ")
    def post(self,request):
        # pdb.set_trace()
        try:
            data = request.data
            serializer = FileListSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "File Uploaded",
                    "data": serializer.data
                    
                })
            return Response({
                "status": 400,
                "message": "something went wrong",
                "data": serializer.errors
            })
        except Exception as e:
            print(e)

