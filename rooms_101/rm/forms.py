from django import forms
from django.contrib.auth.models import User 
from django.forms import ModelForm
from rm.models import RmUser

class RegistrationForm(ModelForm):
    first_name = forms.CharField(label=u"First Name",
        widget=forms.TextInput(attrs={'class': 'input input-text'}),
        required=True)
    last_name = forms.CharField(label=u"last Name",
        widget=forms.TextInput(attrs={'class': 'input input-text'}),
        required=True)
    email = forms.EmailField(label=u"Your Email",
        widget=forms.TextInput(attrs={'class': 'input input-text'}),
        required=True)
    password = forms.CharField(label=u"Your New Password",
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'input input-text'}),
        required=True)
    verify_password = forms.CharField(label=u"Verify Password",
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'input input-text'}),
        required=True)
    
    class Meta:
        model=RmUser
        exclude=('user',)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email Address is already taken')

    def clean(self):
        password=self.cleaned_data['password']
        verify_password=self.cleaned_data['verify_password']
        if password != verify_password:
            raise forms.ValidationError('Passwords ')
        return self.cleaned_data
