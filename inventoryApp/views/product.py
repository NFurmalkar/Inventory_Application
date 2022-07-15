from django.shortcuts import render,redirect
from inventoryApp.forms import productForm
from inventoryApp.models import productModel,registerModel
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def product(request):
    mail = request.session.get('email')
    email = registerModel.objects.get(email=mail)
    productDetail = productModel.objects.filter(profileName__email=email)
    productDetail = getPaginator(request,productDetail)
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['productName']
            newForm = form.save(commit=False)
            newForm.profileName = email
            newForm.save()

            form.save()
    data = {'productDetail':productDetail}
    return render(request,'inventory/product.html',data)

def updateProduct(request,id):
    mail = request.session.get('email')
    email = registerModel.objects.get(email=mail)
    productDetail = productModel.objects.filter(profileName__email=email)
    productById = productModel.objects.get(id=id)

    if request.method == 'POST':
        form = productForm(request.POST,instance=productById)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.profileName = email
            newForm.save()
            form.save()
            return redirect('/product')

    data = {'productById':productById,'productDetail':productDetail}
    return render(request,'inventory/product.html',data)

def deleteProduct(request,id):
    productById = productModel.objects.get(id=id)
    productById.delete()
    return redirect('/product')

def getPaginator(request,modelName):
    paginator = Paginator(modelName,2)
    getPageNumber = request.GET.get('page')
    try:
        modelName = paginator.get_page(getPageNumber)
    except PageNotAnInteger:
        modelName = paginator.page(1)
    except EmptyPage:
        modelName = paginator.page(paginator.num_pages)

    return modelName
