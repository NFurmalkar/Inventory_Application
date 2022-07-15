from django import forms
from inventoryApp.models import registerModel,productModel,purchaseModel,customerModel,stockModel,sellModel,returnPurchaseModel,returnSellModel

class registerForm(forms.ModelForm):
    class Meta:
        model = registerModel
        fields = '__all__'

class productForm(forms.ModelForm):
    class Meta:
        model = productModel
        fields = '__all__'
        exclude = ['profileName']

class purchaseForm(forms.ModelForm):
    class Meta:
        model = purchaseModel
        fields = '__all__'

class customerForm(forms.ModelForm):
    class Meta:
        model = customerModel
        fields = '__all__'
        exclude =['profileName']

class stockForm(forms.ModelForm):
    class Meta:
        model = stockModel
        fields = '__all__'

class sellForm(forms.ModelForm):
    class Meta:
        model = sellModel
        fields = '__all__'

class returnPurchaseForm(forms.ModelForm):
    class Meta:
        model = returnPurchaseModel
        fields ='__all__'

class returnSellForm(forms.ModelForm):
    class Meta:
        model = returnSellModel
        fields='__all__'
        exclude =['sellReturnSellId']
