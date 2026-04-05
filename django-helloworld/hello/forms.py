from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.utils.safestring import mark_safe

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


# Overrides UserCreationForm to add CSS styling
class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

