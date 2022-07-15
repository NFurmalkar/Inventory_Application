from django.shortcuts import render,redirect
from inventoryApp.forms import productForm,sellForm,returnSellForm
from inventoryApp.models import productModel,stockModel,purchaseModel,customerModel,sellModel,returnSellModel
from django.contrib import messages
import random
from  django.http import JsonResponse
import json
from django.db.models import Sum
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def getpaginations(request,ModelName):
    paginator = Paginator(ModelName,2)
    pageNumber = request.GET.get('page')
    try:
        ModelName = paginator.get_page(pageNumber)
    except PageNotAnInteger:
        ModelName = paginator.page(1)
    except EmptyPage:
        ModelName = paginator.page(paginator.num_pages)
    return ModelName

def sales(request):
    return render(request,'inventory/sales.html')

def newSale(request):
    email = request.session.get('email')
    customerData = customerModel.objects.filter(profileName__email=email)
    productData = stockModel.objects.filter(purchaseId__productId__profileName__email=email)
    sellData = sellModel.objects.filter(customerId__profileName__email=email).order_by('-sellDate')
    #print(productData)
    not_unique=True
    invoiceNum=None
    while not_unique:
        list=[]
        for i in range(9):
            list.append(str(random.randint(0,9)))
        invoiceNum = ''.join(list)
        if not sellModel.objects.filter(invoice=invoiceNum):
            not_unique=False
    print(invoiceNum)
    sellData = getpaginations(request,sellData)

#-----------------------------------------POST Method-----------------------
    if request.method == 'POST':
        form = sellForm(request.POST)
        if form.is_valid():
            qty = request.POST.get('quantity')
            id  = request.POST.get('stockId')
            print(qty,id)
            form.save()

            stockData = stockModel.objects.get(id=id)
            mainQty = stockData.quantity
            aftersell = int(mainQty) - int(qty)
            print("aftersell----->",aftersell)
            stockData.quantity = aftersell
            stockData.save()

        print(form.errors)
    data = {'productData':productData,'customerData':customerData,'sellData':sellData,'invoiceNum':invoiceNum}
    return render(request,'inventory/newsale.html',data)

def getProductById(request):
    if request.method == 'POST':
        listData =[]
        dict = {}
        productId = json.loads(request.body)
        #print('productId:',productId)
        id = productId.get('id')
        print("id is:",id)
        stockDataById = stockModel.objects.get(id=id)
        listData.clear()
        dict.clear()
        dict['rate'] = stockDataById.purchaseId.rate
        dict['discount'] = stockDataById.purchaseId.discount
        dict['CGST'] = stockDataById.purchaseId.CGST
        dict['IGST'] = stockDataById.purchaseId.IGST
        dict['quantity'] = stockDataById.quantity
        dict['taxableAmount'] = stockDataById.purchaseId.taxableAmount
        dict['totalAmount'] = stockDataById.purchaseId.totalAmount
        dict['invoice'] = stockDataById.purchaseId.invoice
        listData.append(dict)
        print(listData,dict)
        data =({'productDataById':listData})
        return JsonResponse(data)

def updatesell(request,id):
    email = request.session.get('email')
    sellDataById = sellModel.objects.get(id=id)
    customerData = customerModel.objects.filter(profileName__email=email)
    productData = stockModel.objects.filter(purchaseId__productId__profileName__email=email)
    sellData = sellModel.objects.filter(customerId__profileName__email=email)
    print(sellDataById)
    print(sellDataById.stockId.quantity)
#-------------------------------------------POST Method-----------------------
    if request.method == 'POST':
        pass
    data = {'sellDataById':sellDataById,'customerData':customerData,'productData':productData,'sellData':sellData}
    return render(request,'inventory/newsale.html',data)

def deleteNewSale(request,id):
    pass
    return redirect('/newsale')

def returnSell(request):
    email = request.session.get('email')
    sellData=None
    id=None
    remainingQty=None
    if request.method == 'POST':
        invoiceNo = request.POST.get('invoice')
        try:
            sellData = sellModel.objects.get(invoice=invoiceNo,customerId__profileName__email=email)
            id = sellData.id
            sumOfReturnSell = returnSellModel.objects.filter(sellReturnSellId__invoice=invoiceNo,sellReturnProductId__profileName__email=email).aggregate(Sum('sellReturnQuantity'))
            sumReturnSell = sumOfReturnSell.get('sellReturnQuantity__sum')
            sellquantity = sellData.quantity
            print(sellquantity,sumReturnSell)
            if sumReturnSell and sellquantity:
                print(sellquantity-sumReturnSell)
                remainingQty = sellquantity-sumReturnSell
        except Exception as e:
            messages.error(request,'Records Not Found')
        print(id)
    data = {'sellData':sellData,'remainingQty':remainingQty}
    return render(request,'inventory/sellreturn.html',data)

def returnSellandUpdate(request):
    email = request.session.get('email')
    if request.method=='POST':
        invoiceNo = request.POST.get('sellReturnInvoice')
        quantity = int(request.POST.get('sellReturnQuantity'))
        sellData = sellModel.objects.get(invoice=invoiceNo, customerId__profileName__email=email)
        #print(sellData.stockId)
        Sid=sellData.stockId
        Sid=str(Sid)
        print(type(Sid),Sid)
        form=returnSellForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.sellReturnSellId = sellData
            newForm.save()
            form.save()

            stockData = stockModel.objects.get(id=Sid)
            Sqty = stockData.quantity
            add = Sqty+quantity
            stockData.quantity = add
            stockData.save()
            print(Sqty)
        print(form.errors)

    return redirect('/returnSell')