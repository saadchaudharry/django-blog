from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class log(forms.Form):
    Username =forms.CharField(max_length=120,required=True)
    Password =forms.CharField(max_length=120,required=True)


class Usercreate(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2','is_staff')

    def save(self,commit=True):
        user=super().save(commit=False)

        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.is_staff=self.cleaned_data['is_staff']

        if commit:
            user.save()
        return user