from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm
)
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Customer


# =========================
# CUSTOMER REGISTRATION FORM
# =========================
class CustomerRegistrationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# =========================
# LOGIN FORM
# =========================
class LoginForm(AuthenticationForm):

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control'
            }
        )
    )


# =========================
# PASSWORD CHANGE FORM
# =========================
class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label='Old Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'autofocus': True,
                'class': 'form-control'
            }
        )
    )

    new_password1 = forms.CharField(
        label='New Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control'
            }
        ),
        help_text=password_validation.password_validators_help_text_html()
    )

    new_password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control'
            }
        )
    )


# =========================
# CUSTOMER PROFILE FORM
# =========================
class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }
