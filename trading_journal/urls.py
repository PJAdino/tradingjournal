from django.urls import path
from . import views
from .views import CurrencyPairView
from django.contrib.auth.views import LoginView

urlpatterns=[
    path("home/", views.home, name='home'),
    path("new_trade/", CurrencyPairView.as_view() , name='new_trade'),
    path("trades/", views.display_trades, name='trades'),
    
]