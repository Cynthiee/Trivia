from django import forms
from .models import User

class WaitlistForm(forms.ModelForm):
    referral_code = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'referral_code']
