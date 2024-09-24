from django import forms
from . models import Contact
from django . forms import Textarea,TextInput,Select

class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields =['name','phone','email','message']

        widgets ={
            'name':TextInput(attrs={
            "type":"text",
            "class":"form-control",
            "id":"inputName4", 
            "placeholder":"Name",
            }),
            'phone':TextInput(attrs={
            "type":"text", 
            "class":"form-control", 
            "id":"inputSubject4",
            "placeholder":"Phone",
            }),
            'email':TextInput(attrs={
            "type":"email",
            "class":"form-control", 
            "id":"inputEmail4", 
            "placeholder":"Email id",
            }),
            'message':TextInput(attrs={
            "type":"text",
            "class":"form-control", 
            "id":"inputMessage", 
            "placeholder":"Message",
            })
    }