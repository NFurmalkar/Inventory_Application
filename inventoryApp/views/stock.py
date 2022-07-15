from django.shortcuts import render,redirect
from inventoryApp.models import stockModel,registerModel
from django.contrib import messages

def stock(request):
    mail = request.session.get('email')
    email = registerModel.objects.get(email=mail)
    stockData = stockModel.objects.filter(purchaseId__productId__profileName=email)
    params = {'stockData':stockData}
    return render(request,'inventory/stock.html',params)