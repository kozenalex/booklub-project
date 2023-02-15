from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['telegram']
