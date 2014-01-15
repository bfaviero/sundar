from django import forms
from django.contrib.auth import authenticate

class UserForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

    def clean(self):
         email = self.cleaned_data.get('email')
         password = self.cleaned_data.get('password')
         user = authenticate(email=email, password=password)
         if not user or not user.is_active:
             raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
         return self.cleaned_data

    def login(self, request):
         username = self.cleaned_data.get('username')
         password = self.cleaned_data.get('password')
         user = authenticate(email=email, password=password)
         return user