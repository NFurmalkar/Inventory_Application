from django.contrib import admin
from django.urls import path
from inventoryApp.middleware import VerifyMiddleware
from inventoryApp.views import register,home,product,purchase,saleDetail,customer,forgetpassword,stock
urlpatterns = [
    path('',register.login),
    path('register/',register.register),
    path('otp/',register.otp),
    path('home/',VerifyMiddleware(home.home)),
    path('product/',VerifyMiddleware(product.product)),
    path('updateProduct/<id>',VerifyMiddleware(product.updateProduct)),
    path('deleteProduct/<id>',VerifyMiddleware(product.deleteProduct)),
    path('purchase/',VerifyMiddleware(purchase.purchase)),
    path('purchase/<id>',VerifyMiddleware(purchase.purchaseById)),
    path('updatePurchase/<id>',VerifyMiddleware(purchase.updatePurchase)),
    path('deletePurchase/<id>',VerifyMiddleware(purchase.deletePurchase)),

    path('stock/',VerifyMiddleware(stock.stock)),

    path('sales/',VerifyMiddleware(saleDetail.sales)),
    path('newsale/',VerifyMiddleware(saleDetail.newSale)),
    path('getProductById/',VerifyMiddleware(saleDetail.getProductById)),
    path('updatesell/<id>',VerifyMiddleware(saleDetail.updatesell)),
    path('deleteNewSale/<id>',VerifyMiddleware(saleDetail.deleteNewSale)),

    path('customer/',VerifyMiddleware(customer.customer)),
    path('updateCustomer/<id>',VerifyMiddleware(customer.updateCustomer)),
    path('deleteCustomer/<id>',VerifyMiddleware(customer.deleteCustomer)),

    path('returnPurchase/',VerifyMiddleware(purchase.returnPurchase)),
    path('returnPurchaseAndUpdate/',VerifyMiddleware(purchase.returnPurchaseAndUpdate)),
    path('returnSell/',VerifyMiddleware(saleDetail.returnSell)),
    path('returnSellandUpdate/',VerifyMiddleware(saleDetail.returnSellandUpdate)),

    path('forgetpassword/',forgetpassword.forgetPassword)

]