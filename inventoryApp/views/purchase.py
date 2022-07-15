from django.shortcuts import render,redirect
from inventoryApp.forms import purchaseForm,stockForm,returnPurchaseForm
from inventoryApp.models import purchaseModel,registerModel,productModel,customerModel,stockModel,returnPurchaseModel
from django.contrib import messages
import datetime
from django.db.models import Sum,Count
import json
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def getpagination(request,ModelName):
    paginator = Paginator(ModelName,2)
    pageNumber = request.GET.get('page')
    try:
        ModelName = paginator.get_page(pageNumber)
    except PageNotAnInteger:
        ModelName = paginator.page(1)
    except EmptyPage:
        ModelName = paginator.page(paginator.num_pages)
    return ModelName

def purchase(request):
    purchaseDetail = None
    email = request.session.get('email')
    productData = productModel.objects.filter(profileName__email=email)
    customerData = customerModel.objects.filter(profileName__email=email)

    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    print(startDate,endDate)
    if startDate and endDate:
        purchaseDetail = purchaseModel.objects.filter(purchaseDate__gte=startDate,purchaseDate__lte=endDate,productId__profileName__email=email).order_by('-purchaseDate')
        print("startdate and end:", type(purchaseDetail), purchaseDetail)
    elif startDate:
        purchaseDetail = purchaseModel.objects.filter(purchaseDate__gte=startDate,productId__profileName__email=email).order_by('-purchaseDate')
        print("startdate:",type(purchaseDetail), purchaseDetail)
    elif endDate:
        purchaseDetail = purchaseModel.objects.filter(purchaseDate__lte=endDate,productId__profileName__email=email).order_by('-purchaseDate')
        print("end Date:",type(purchaseDetail), purchaseDetail)

    if startDate == '' and endDate == '':
        purchaseDetail = purchaseModel.objects.filter(productId__profileName__email=email).order_by('-purchaseDate')
    if startDate == None and endDate == None:
        purchaseDetail = purchaseModel.objects.filter(productId__profileName__email=email).order_by('-purchaseDate')
    totalSum = purchaseDetail.aggregate(Sum('rate'),Sum('quantity'),Sum('CGST'),Sum('IGST'),Sum('totalAmount'),Sum('taxableAmount'))

    purchaseDetail = getpagination(request,purchaseDetail)
    if request.method == 'POST':
        form = purchaseForm(request.POST)
        if form.is_valid():
            getDate = None
            getDate = request.POST.get('purchaseDate')
            if getDate == '':
                getDate = datetime.datetime.now()
            newForm = form.save(commit=False)
            newForm.purchaseDate = getDate
            newForm.save()
            form.save()


            return redirect('/purchase')
        print("form error:",form.errors)

    data = {'productData':productData,'customerData':customerData,'purchaseDetail':purchaseDetail,'totalSum':totalSum}
    return render(request,'inventory/purchase.html',data)


def purchaseById(request,id):
    email = request.session.get('email')
    productData = productModel.objects.filter(profileName__email=email)
    customerData = customerModel.objects.filter(profileName__email=email)

    purchaseDetail = purchaseModel.objects.filter(productId__profileName__email=email).order_by('-purchaseDate')
    totalSum = purchaseDetail.aggregate(Sum('rate'),Sum('quantity'),Sum('CGST'),Sum('IGST'),Sum('totalAmount'),Sum('taxableAmount'))

    getproductById = productModel.objects.get(id=id)

    if request.method == 'POST':
        form = purchaseForm(request.POST)
        if form.is_valid():
            f=form.save()
            #print("f value:", f.id,f.purchaseDate)
            stockData = purchaseModel.objects.get(id=f.id)
            #print(stockData,stockData.id,stockData.quantity,stockData.purchaseDate)
            stocktoSave = stockModel(purchaseId=stockData,date=stockData.purchaseDate,quantity=stockData.quantity)
            stocktoSave.save()

            return redirect('/purchase')
        print("form error:", form.errors)

    data = {'productData':productData,'customerData':customerData,'purchaseDetail':purchaseDetail,'totalSum':totalSum,'getproductById':getproductById}
    return render(request,'inventory/purchase.html',data)


def updatePurchase(request,id):
    global instanceValue
    global pID
    global stockdata
    email = request.session.get('email')
    productData = productModel.objects.filter(profileName__email=email)
    customerData = customerModel.objects.filter(profileName__email=email)
    purchaseDetail = purchaseModel.objects.filter(productId__profileName__email=email).order_by('-purchaseDate')
    totalSum = purchaseDetail.aggregate(Sum('rate'), Sum('quantity'), Sum('CGST'), Sum('IGST'), Sum('totalAmount'),
                                        Sum('taxableAmount'))
    getproductById = None #productModel.objects.get(id=id)
    purchaseDetails = None

    try:
        purchaseDetails = purchaseModel.objects.get(id=id)
        instanceValue = purchaseDetails
        stockdata = stockModel.objects.get(purchaseId=id)
    
    except Exception as e:
        getproductById = productModel.objects.get(id=id)

    print("getproductById:",getproductById)
    print("purchaseDetails:",purchaseDetails)
    print("purchaseDetails value is:",instanceValue)
    if request.method == 'POST':
        #print("purchaseData",instanceValue)
        form = purchaseForm(request.POST,instance=instanceValue)
        if form.is_valid():
            f=form.save()
            if stockdata is not None:
                stockdata.date = f.purchaseDate
                stockdata.quantity = f.quantity
                stockdata.save()
            return redirect('/purchase')
        print(form.errors)

    data = {'productData':productData,'customerData':customerData,'purchaseDetail':purchaseDetail,'totalSum':totalSum,'getproductById':getproductById,
            'purchaseDetails':instanceValue}
    return render(request,'inventory/purchase.html',data)


def deletePurchase(request,id):
    getData = purchaseModel.objects.get(id=id)
    getData.delete()
    return redirect('/purchase')

#-----------------------------------------------Return purchase-------------------------

def returnPurchase(request):
    email = request.session.get('email')
    getStockData=None
    if request.method == "POST":
        invoice = request.POST.get('invoice')
        print(invoice)
        getStockData = stockModel.objects.filter(purchaseId__invoice=invoice,purchaseId__customerId__profileName__email=email)
        if not getStockData:
            messages.success(request,"Records Not Found")
        print("getStockData--->", getStockData)
    data = {'getStockData':getStockData}
    return render(request, 'inventory/purchasereturn.html',data)

def returnPurchaseAndUpdate(request):
    if request.method == 'POST':
        stockId = request.POST.get('purchaseReturnId')
        userQty = request.POST.get('returnQuantity')
        customerId = request.POST.get('custNameId')
        userDate = request.POST.get('purchaseReturnDate')

        print("stockId is---------->",stockId)
        print("userQty is---------->",userQty,"customerId is-->",customerId)
        changeData = stockModel.objects.get(id=stockId)
        print("id",changeData.id)
        #print("quantity",changeData.purchaseId.quantity)
        #print("totalAmount IN PURCHASE",changeData.purchaseId.totalAmount)
        #purchaseModel_totalAmount = changeData.purchaseId.totalAmount
        #purchaseModel_rate = changeData.purchaseId.rate
        #purchaseModel_discount = changeData.purchaseId.discount
        purchaseModel_quantity = changeData.quantity
        remainingQty = int(purchaseModel_quantity) - int(userQty)
        print(purchaseModel_quantity,"Remaining qty--->",remainingQty)
        form = returnPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            changeData.quantity=remainingQty
            changeData.save()


        print(form.errors)
        #saveData = returnPurchaseModel(purchaseReturnId=stockId,custNameId=customerId,purchaseReturnDate=userDate,returnQuantity=userQty)
        #saveData.save()



        return redirect('/returnPurchase')

    return redirect('/returnPurchase')







"""
def returnPurchase(request):
    email = request.session.get('email')
    if request.method == "POST":
        data = json.loads(request.body)
        invoice = data.get('invoice')
        print(data,invoice)
        getStockData = stockModel.objects.filter(purchaseId__invoice=invoice,purchaseId__customerId__profileName__email=email)
        print("getStockData--->",getStockData)
        getStockData = list(getStockData.values())
        print("getStockDataWith values--->", getStockData)
        if len(getStockData) == 0:
            return JsonResponse({"Error404":"404"})
        data = {'getStockData':getStockData}
        return JsonResponse(data)

    return render(request,'inventory/purchasereturn.html')
"""