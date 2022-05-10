from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
 

class OrderingForm(ModelForm):
    class Meta:
        model = Ordering
        fields= '__all__'
        labels = {
             'deadline':'Deadline eg 01/01/2022 12:00',
             
           
             }
class OrderingForm(ModelForm):
    class Meta:
        model = Ordering
        fields= '__all__'
        labels = {
             'deadline':'Deadline eg 01/01/2022 12:00',
             
           
             }
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user' ]

class TaskForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		