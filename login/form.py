from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','is_active']
        widgets = {
            'username':TextInput(attrs={'class':'form-control'}),
            'password':PasswordInput(attrs={'class':'form-control'})
        }

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_active','date_joined']
        widgets = {
            'username':TextInput(attrs={'class':'form-control'}),
            'first_name':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control'}),
            'date_joined':TextInput(attrs={'class':'form-control'}),
        }