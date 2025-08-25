from .models import usermodel
import re
from django import forms
from django.forms import ModelForm

class userform(ModelForm):
    class Meta:
        model = usermodel
        fields = ['first_name','last_name','user_name','user_mail','password']
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'user_name':'Username',
            'user_mail':'E-Mail',
            'password':'Password'
        }
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'Your First Name Here'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Your Last Name Here'}),
            'user_name':forms.TextInput(attrs={'placeholder':'Select Your Username'}),
            'user_mail':forms.EmailInput(attrs={'placeholder':'Your Mail'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Secret Here'}),

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'w-full px-3 py-2 rounded bg-gray-900 text-white border border-gray-700 focus:outline-none focus:border-orange-500'})

    def clean_user_name(self):
        username = self.cleaned_data['user_name']
        if not re.match(r'^[A-Za-z0-9_]+$', username):
            raise forms.ValidationError("Username may only contain letters, numbers, and underscores.")
        return username

    # def clean_password(self):
    #     password = self.cleaned_data['password']

    #     if len(password) < 8:
    #         raise forms.ValidationError("Password must be at least 8 characters long.")
    #     if not re.search(r'[A-Z]', password):
    #         raise forms.ValidationError("Password must contain at least one uppercase letter.")
    #     if not re.search(r'[a-z]', password):
    #         raise forms.ValidationError("Password must contain at least one lowercase letter.")
    #     if not re.search(r'\d', password):
    #         raise forms.ValidationError("Password must contain at least one number.")
    #     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    #         raise forms.ValidationError("Password must contain at least one special character (!@#$ etc).")

    #     return password