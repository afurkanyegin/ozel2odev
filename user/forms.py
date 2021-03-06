from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, FileInput, EmailInput
from django import forms

from Home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email')
        widgets = {
            'username'  : TextInput(attrs={'class':'input','placeholder':'username'}),
            'first_name': TextInput(attrs={'class':'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class':'input','placeholder':'last_name'}),
            'email'     : EmailInput(attrs={'class':'input','placeholder':'email'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = ('phone','address','city','country','image')
        widgets = {
            'phone'   : TextInput(attrs={'class':'input','placeholder':'phone'}),
            'address' : TextInput(attrs={'class':'input','placeholder':'address'}),
            'city'    : TextInput(attrs={'class':'input','placeholder':'city'}),
            'country' : TextInput(attrs={'class':'input','placeholder':'country'}),
            'image'   : FileInput(attrs={'class':'input','placeholder':'image'}),
        }
