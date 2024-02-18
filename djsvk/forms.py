from django import forms

class usersform(forms.Form):
    email=forms.EmailField()
    passw=forms.PasswordInput()
    addr=forms.CharField()
    city=forms.CharField()
    zip=forms.IntegerField()