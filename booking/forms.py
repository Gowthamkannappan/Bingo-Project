from django import forms
from .models import Booking


class Form(forms.ModelForm):
     class Meta(object):
        model = Booking
        fields = "__all__"
