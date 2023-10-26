from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class CurrencyPair(models.Model):
    """The currency pair user will trade"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pair = models.CharField(max_length=6)
    opening_price = models.FloatField()
    closing_price = models.FloatField()
    take_profit = models.FloatField()
    stop_loss = models.FloatField()
    lot_size = models.FloatField()
    trade_screenshort = models.ImageField(upload_to ='uploads', null= True) 
    date_added = models.CharField(max_length=10)
    reason =  models.TextField(max_length=200)
    result = models.FloatField()
    date = models.DateTimeField(auto_now=True)
