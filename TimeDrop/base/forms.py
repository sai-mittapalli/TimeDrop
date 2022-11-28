from django import forms
from django.forms import ModelForm
from .models import Event
from .models import CalendarSave
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):

    eventName = forms.CharField(
        max_length=200,
        widget = forms.TextInput(attrs={
            'class':'eventName', 
            'placeholder':'Enter Title'
            })
    )

    dueDate = forms.DateField(
        widget = forms.TextInput(attrs={
            'class':'dueDate', 
            'placeholder':'Enter Due Date'
            })
    )  

    eventTime = forms.TimeField(
        widget = forms.TextInput(attrs={
            'class':'eventTime', 
            'placeholder':'Enter Time Due'
            })
    )  

    eventDescription = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'eventDescription', 
            'placeholder':'Enter Description',
            'style': 'background-color: #262a35;'
            })
    )  

    class Meta:
        model = Event
        fields = ["eventName", "dueDate", "eventTime", "eventDescription"]
        labels = {'Event Name': "eventName", 'Due Date': "dueDate", 'Due Time': "eventTime", 'Event Description': "eventDescription"}


class CalendarForm(forms.ModelForm):

    calendarName = forms.CharField(
        max_length=50,
        widget = forms.TextInput(attrs={
            'class':'calendarName', 
            'placeholder':'Enter Name',
            'style': 'border: solid 1px #262a35; width: 250px; height: 50px; padding: 10px; margin: 5%; background-color: #262a35; border-radius: 25px; color: white;'
            })
    )

    #calendarColor = forms.CharField(
     #   widget = ColorPickerWidget) 

    class Meta:
        model = CalendarSave
        fields = ["calendarName"]


class SignUpForm(UserCreationForm):
    firstName = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'class':'firstName', 'placeholder':'First Name'})
    )

    lastName = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'class':'lastName', 'placeholder':'Last Name'})
    )

    email = forms.EmailField(
        max_length=150,
        widget = forms.TextInput(attrs={'class':'email', 'placeholder':'Email'})    
    )

    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'username', 'placeholder':'Username'})
    )

    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'pass', 'placeholder':'Password'})
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'pass', 'placeholder':'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'username', 'password1', 'password2')

