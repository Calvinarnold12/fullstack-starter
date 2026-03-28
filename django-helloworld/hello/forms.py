from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


# Overrides AuthenticationFrom to add CSS styling
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg'}
    ))
