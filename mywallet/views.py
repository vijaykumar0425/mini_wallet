from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class InitializeAccountApiView(APIView):

    def post(self, request):
        serializer = serializers.AccountInitializeSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.create_user_token()
            if token:
                return Response({"data": {"token": token}, "status": "success"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"data": {"error": "Customer Not Found"}, "status": "fail"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"data": {"error": serializer.errors}, "status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)


class WalletApiView(APIView):
    permission_classes = ()

    def get(self, request):
        wallet = request.user.get_wallet()
        if wallet.is_disabled:
            return Response({"data": {"error": "Disabled"}, "status": "fail"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.WalletSerializer(wallet)
        return Response({"data": {"wallet": serializer.data}, "status": "success"}, status=status.HTTP_200_OK)

    def post(self, request):
        wallet = request.user.get_wallet()
        if wallet.is_disabled:
            wallet.is_disabled = False
            wallet.save(update_fields=['is_disabled'])
            serializer = serializers.WalletSerializer(wallet)
            return Response({"data": {"wallet": serializer.data}, "status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"data": {"error": "Already enabled"}, "status": "fail"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        pass


class DepositAmountApiView(APIView):
    def post(self, request):
        amount = request.data.get('amount', None)


class WithdrawAmountApiView(APIView):

    def post(self, request):
        amount = request.data.get('amount', None)
