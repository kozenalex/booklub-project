from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import ClearableFileInput
from users.models import MyUser


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'avatar', 'first_name', 'last_name', 'email', 'telegram']

class UserUpdateForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'telegram']

class MyAvaWidget(ClearableFileInput):

    initial_text = ''
    input_text = 'Загрузить новый аватар'
    

class UserAvaUpdateForm(forms.ModelForm):


    
    class Meta(MyAvaWidget):

        model = MyUser
        fields = ['avatar']
        labels = {'avatar': ''}
        widgets = {
           'avatar': MyAvaWidget() 
        }
        