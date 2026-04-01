from .models import OrderReview, Profile, Order
from django.contrib.auth.models import User
from django import forms

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
