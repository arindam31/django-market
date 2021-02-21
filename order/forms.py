from django import forms
from order.models import CartItem


class EditCartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
