from django.urls import path
from . import views

urlpatterns = [
    path('init', views.InitializeAccountApiView.as_view(), name='initialize'),
    path('wallet', views.WalletApiView.as_view(), name='wallet'),
    path('wallet/deposits', views.DepositAmountApiView.as_view(), name='deposit'),
    path('wallet/withdrawals', views.WithdrawAmountApiView.as_view(), name='withdraw'),

]
