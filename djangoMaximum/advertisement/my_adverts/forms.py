from django import forms
from django.forms import ModelForm
from .models import Advertisement

# Вариант 1
# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64,
#         widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control form-control-lg'}))
#     photo = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control form-control-sm'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}))
#     category = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))

# Вариант 2
class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'photo', 'price', 'category', 'auction')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control form-control-lg'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control form-control-lg'}),
            'photo' : forms.FileInput(attrs={'class' : 'form-control form-control-sm'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}),
            'category' : forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}),
            'auction' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        }
        required = {
            'auction' : False,
            'photo' : False,
        }