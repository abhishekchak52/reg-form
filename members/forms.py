from django import forms
from .models import member

class MemberForm(forms.ModelForm):
    class Meta:
        model = member
        exclude = ['timestamp']
        labels = {
            'name':"FULL NAME",
            'course':"COURSE",
            'year':"YEAR",
            'phone_number':"PHONE NUMBER",
            'email':"EMAIL",
            'message':"MESSAGE",
        }
