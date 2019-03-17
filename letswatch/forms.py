from django import forms
from django.contrib.auth.models import User
from letswatch.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

#An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, label="")

    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('password',)
