from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


# Create your views here.


class WalletApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        wallet = request.user.get_wallet()
        if wallet is None or wallet.is_disabled:
            return Response({"data": {"error": "Disabled"}, "status": "fail"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.WalletSerializer(wallet)
        return Response({"data": {"wallet": serializer.data}, "status": "success"}, status=status.HTTP_200_OK)

    def post(self, request):
        wallet = request.user.get_wallet()
        if wallet.is_disabled:
            wallet.is_disabled = False
            wallet.enabled_at = timezone.now()
            wallet.save(update_fields=['is_disabled', 'enabled_at'])
            serializer = serializers.WalletSerializer(wallet)
            return Response({"data": {"wallet": serializer.data}, "status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"data": {"error": "Already enabled"}, "status": "fail"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        instance = request.user.get_wallet()
        serializer = serializers.WalletSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": {"wallet": serializer.data}, "status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": {"error": serializer.errors}, "status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)


class DepositAmountApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        amount = request.data.get('amount', None)
        success, error_msg = True, None
        if (not amount) or (amount <= 0):
            success = False
            error_msg = "Invalid amount."
        wallet = request.user.get_wallet()
        if success:
            if not wallet:
                success = False
                error_msg = "Wallet does not exist for user."
            elif wallet.is_disabled:
                success = False
                error_msg = "Disabled"
        if success:
            wallet.deposit(amount)
            data = serializers.WalletSerializer(wallet).data
            data["amount"] = amount
            return Response({"data": {"deposit": data}, "status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": {"error": error_msg}, "status": "fail"}, status=status.HTTP_404_NOT_FOUND)


class WithdrawAmountApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        amount = request.data.get('amount', None)
        success, error_msg = True, None
        if (not amount) or (amount <= 0):
            success = False
            error_msg = "Invalid amount."
        wallet = request.user.get_wallet()
        if success:
            if not wallet:
                success = False
                error_msg = "Wallet does not exist for user."
            elif wallet.is_disabled:
                success = False
                error_msg = "Disabled"
        if success:
            wallet.withdraw(amount)
            data = serializers.WalletSerializer(wallet).data
            data["amount"] = amount
            return Response({"data": {"deposit": data}, "status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": {"error": error_msg}, "status": "fail"}, status=status.HTTP_404_NOT_FOUND)
