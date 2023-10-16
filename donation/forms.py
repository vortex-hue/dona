from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'seed', 'amount', 'message']

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'comment-form__input-box',
            'placeholder': 'Your name'
        })
    )
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'comment-form__input-box',
            'placeholder': 'Email address'
        })
    )
    
    seed = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'comment-form__input-box',
            'placeholder': 'Seed (seed is never stored)',
            'name': 'seed'
        })
    )

    amount = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class': 'comment-form__input-box',
            'placeholder': 'Donation amount',
            'name':'xrp_amount'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'comment-form__input-box',
            'placeholder': 'Leave a message'
        })
    )
