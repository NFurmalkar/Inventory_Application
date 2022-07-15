from django import template
from inventoryApp.models import productModel,customerModel

register = template.Library()

@register.filter(name="getSaleDetails")
def getSaleDetails(value):
    value = value.id
    getData = productModel.objects.get(id=value)
    #print(getData.productName)
    return getData.productName

@register.filter(name="getCustomerName")
def getCustomerName(value):
    value = value.id
    getData = customerModel.objects.get(id=value)
    return getData.customerName
