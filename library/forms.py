from django import forms
from .models import Userregistration
from .models import addbookdetails

class StudRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Userregistration
        fields = "__all__"

class AddBookForm(forms.ModelForm):
    
    class Meta:
        model = addbookdetails
        fields = "__all__"
        