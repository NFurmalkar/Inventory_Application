from django.db import models
import datetime
# Create your models here.

class registerModel(models.Model):
    firstname = models.CharField(max_length=70)
    lastName = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    gender = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.email

class customerModel(models.Model):
    profileName = models.ForeignKey(registerModel, on_delete=models.CASCADE)
    customerName = models.CharField(max_length=100)
    address = models.CharField(max_length=100,blank=True,null=True)
    mobileNumber = models.IntegerField(blank=True, null=True)
    GSTno = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        id = str(self.id)
        return id

class productModel(models.Model):
    profileName = models.ForeignKey(registerModel,on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    discount = models.IntegerField(default=0,blank=True, null=True)
    CGST = models.IntegerField(default=0,blank=True, null=True)
    SGST = models.IntegerField(default=0,blank=True, null=True)
    IGST = models.IntegerField(default=0,blank=True, null=True)
    productDescription = models.CharField(max_length=900,blank=True,null=True)
    def __str__(self):
        id = str(self.id)
        return id

class purchaseModel(models.Model):
    productId = models.ForeignKey(productModel, on_delete=models.CASCADE)
    customerId = models.ForeignKey(customerModel, on_delete=models.CASCADE)
    purchaseDate = models.DateTimeField(default=datetime.datetime.today(),blank=True,null=True)
    invoice = models.CharField(max_length=100)
    rate = models.IntegerField()
    quantity = models.BigIntegerField()
    discount = models.IntegerField(blank=True,null=True)
    CGST = models.IntegerField(blank=True,null=True)
    IGST = models.IntegerField(blank=True,null=True)
    taxableAmount = models.IntegerField(default=0,blank=True,null=True)
    totalAmount = models.BigIntegerField()

    def __str__(self):
        id = str(self.id)
        return id

class stockModel(models.Model):
    purchaseId = models.ForeignKey(purchaseModel,on_delete=models.CASCADE)
    date = models.DateTimeField()
    quantity = models.IntegerField()

    def __str__(self):
        id = str(self.id)
        return id

class sellModel(models.Model):
    stockId = models.ForeignKey(stockModel,on_delete=models.CASCADE)
    customerId = models.ForeignKey(customerModel,on_delete=models.CASCADE)
    sellDate = models.DateTimeField()
    invoice = models.CharField(max_length=100)
    rate = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.FloatField()
    CGST = models.FloatField()
    IGST = models.FloatField()
    taxableAmount = models.IntegerField()
    totalAmount = models.BigIntegerField()

    def __str__(self):
        id = str(self.id)
        return id

class returnPurchaseModel(models.Model):
    purchaseReturnId = models.ForeignKey(stockModel,on_delete=models.CASCADE)
    custNameId = models.ForeignKey(customerModel,on_delete=models.CASCADE)
    purchaseReturnDate = models.DateTimeField()
    returnQuantity = models.IntegerField()

class returnSellModel(models.Model):
    sellReturnProductId = models.ForeignKey(productModel,on_delete=models.CASCADE)
    sellReturnSellId = models.ForeignKey(sellModel, on_delete=models.CASCADE)
    sellReturnDate = models.DateTimeField()
    sellReturnQuantity = models.IntegerField()




