from django.forms import BaseFormSet

from .models import OrderReview, Profile, Order
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderLine


class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'due_back']
        # Dėstytojo metodas: tiesiog nurodom 'type': 'date'
        widgets = {
            'due_back': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
OrderLineFormSet = inlineformset_factory(
    Order,          # Pagrindinis modelis
    OrderLine,      # Modelis, kurio eilučių norime
    fields=('service', 'quantity'), # Kokie stulpeliai bus eilutėje
    extra=3,        # Kiek tuščių eilučių rodyti iškart
    can_delete=True # Ar leisti ištrinti eilutę redaguojant
)