"""Forms of the project."""
from django import forms
from django.forms import Form, ModelForm
from django import forms
from .models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
        widgets = {"description": forms.Textarea(), "quantity": forms.NumberInput()}

     
