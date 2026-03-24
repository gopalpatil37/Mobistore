from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile name'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter brand'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'ram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 8GB'
            }),
            'storage': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 128GB'
            }),
            'processor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter processor'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }