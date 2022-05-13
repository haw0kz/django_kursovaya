from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    description =forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control'}))
