from django.shortcuts import render,redirect
from inventoryApp.models import customerModel,registerModel
from inventoryApp.forms import customerForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.db.models import Sum

def customer(request):
    mail = request.session.get('email')
    email = registerModel.objects.get(email=mail)
    customerDetail = customerModel.objects.filter(profileName__email=email)

    #----call paginator function ----
    customerDetail = getpagination(request,customerDetail)

    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.profileName = email
            newForm.save()

            form.save()
            return redirect('/customer')
    data =  {'customerDetail':customerDetail}
    return render(request,'inventory/customer.html',data)


def updateCustomer(request,id):
    mail = request.session.get('email')
    email = registerModel.objects.get(email=mail)
    customerDetail = customerModel.objects.filter(profileName__email=email)

    customerData = customerModel.objects.get(id=id)
    # ----call paginator function ----
    customerDetail = getpagination(request, customerDetail)

    if request.method == 'POST':
        form = customerForm(request.POST,instance=customerData)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.profileName = email
            newForm.save()

            form.save()
            return redirect('/customer')
        print("Form error",form.errors)

    data = {'customerDetail':customerDetail,'customerData':customerData}
    return render(request,'inventory/customer.html',data)

def deleteCustomer(request,id):
    #print("delete id ",id,type(id))
    customerData = customerModel.objects.get(id=id)
    customerData.delete()
    return redirect('/customer')


def getpagination(request,ModelName):
    # -----Paginator--------
    paginator = Paginator(ModelName, 2)
    pageNumber = request.GET.get('page')
    try:
        ModelName = paginator.get_page(pageNumber)
    except PageNotAnInteger:
        ModelName = paginator.page(1)
    except EmptyPage:
        ModelName = paginator.page(paginator.num_pages)
    return ModelName
