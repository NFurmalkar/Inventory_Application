from django.shortcuts import render
from inventoryApp.models import productModel,purchaseModel,customerModel,sellModel,returnSellModel,returnPurchaseModel
from django.db.models import Sum,Count

def home(request):
    email = request.session.get('email')
    totalCustomer = customerModel.objects.filter(profileName__email=email).aggregate(Count('id'))
    toalProduct = productModel.objects.filter(profileName__email=email).aggregate(Count('id'))
    totalPurchase = purchaseModel.objects.filter(productId__profileName__email=email).aggregate(Count('id'))
    totalSell = sellModel.objects.filter(customerId__profileName__email=email).aggregate(Count('id'))
    totalPurchaseReturn = returnPurchaseModel.objects.filter(custNameId__profileName__email=email).aggregate(Count('id'))
    totalSellReturn = returnSellModel.objects.filter(sellReturnProductId__profileName__email=email).aggregate(Count('id'))
    print(totalSellReturn)
    data = {'totalCustomer':totalCustomer,'toalProduct':toalProduct,'totalPurchase':totalPurchase,'totalSell':totalSell,
            'totalPurchaseReturn':totalPurchaseReturn,'totalSellReturn':totalSellReturn}
    return render(request,'inventory/home.html',data)