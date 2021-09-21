from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


# Create your views here.

class InitializeAccountApiView(APIView):

    def post(self, request):
        serializer = serializers.AccountInitializeSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.create_user_token()
            print(type(token))
            if token:
                return Response({"data": {"token": token}, "status": "success"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"data": {"error": "Customer Not Found"}, "status": "fail"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"data": {"error": serializer.errors}, "status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)
