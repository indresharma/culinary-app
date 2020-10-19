from django import forms


from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['tags'].required = False
        self.fields['product_discount'].initial = 0


class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = "__all__"


class RMStockForm(forms.ModelForm):
    class Meta:
        model = RMStock
        fields = "__all__"
        widgets = {
            'validity': forms.TextInput(attrs={'type': 'date'})
        }

class RMStockUpdateForm(forms.ModelForm):
    class Meta:
        model = RMStock
        fields = "__all__"
        widgets = {
            'validity': forms.TextInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(RMStockUpdateForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].disabled = True


    

