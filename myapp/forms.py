from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from .models import User , Activities ,Excursions , Order  


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username' , 'email' , 'password1', 'password2']

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activities 
        fields = ['address' , 'name_activities','A_image','A_Text','price']

class ExcursiosForm(forms.ModelForm):
    # more_images = forms.FileField(required=False , widget=forms.FileInput(attrs={
    #     "class":"form-control",
    #     "multiple":True
    # }))
    class Meta: 
        model = Excursions  
        fields = ['address_E'    , 'name_E','image_E','Text_E','price_E'   ]

class Chekoutform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_name"  ,"namber_room" , "Date_dipart",  ]
        pass
class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class HotilLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

'''

class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ActiviterecherForm(forms.Form):
    class Meta: 
        model =  Cars_Trip
        fields = ['start_V' , 'type_Car' ,'name_Car','Plas','Price','detail' ]
'''