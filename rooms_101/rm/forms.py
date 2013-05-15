from django import forms
from django.contrib.auth.models import User 
from django.forms import ModelForm
from rm.models import GbUser
   
class RegistrationForm(ModelForm):
    GENDER = (
        ('', 'Select-One'),
        ('F', "Male"),
        ('M', "Femail"), 
        )

    first_name = forms.CharField(label=u"First Name",
        widget=forms.TextInput(attrs={'class': 'input input-text span2', 'placeholder': 'First Name'}),
        required=True)
    last_name = forms.CharField(label=u"last Name",
        widget=forms.TextInput(attrs={'class': 'input input-text pull-right span2', 'placeholder': 'Last Name'}),
        required=True)
    email = forms.EmailField(label=u"Your Email",
        widget=forms.TextInput(attrs={'class': 'input input-text  input-block-level', 'placeholder': 'Your Email'}),
        required=True)
    password = forms.CharField(label=u"Your New Password",
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'input input-text input-block-level', 'placeholder': 'New password'}),
        required=True)
    verify_password = forms.CharField(label=u"Verify Password",
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'input input-text  input-block-level', 'placeholder': 'Verify password'}),
        required=True)
    gender = forms.ChoiceField(label=u"Your Gender", choices=GENDER,
        widget=forms.Select(attrs={'class': 'input input-text  input-block-level', 'placeholder': 'Your Gender'}),
        required=True)
    birthdate = forms.DateField(widget=forms.TextInput(attrs={'class': 'input input-text  input-block-level', 'placeholder': 'Your Birth Date'}), required=True)
    
    class Meta:
        model=GbUser
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

class LoginForm(forms.Form):
    email = forms.EmailField(label=u"Your Email",
        widget=forms.TextInput(attrs={'class': 'input input-text input-block-level', 'placeholder': 'Your email'}),
        required=True)
    password = forms.CharField(label=u"Your New Password",
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'input input-text input-block-level', 'placeholder': 'Your password'}),
        required=True)

class CommitGoalForm(forms.Form):
    goal_attr = {"rows": "2", 
                     "class": "input-block-level rm-borderless",
                     "placeholder": "What is your goal?"}
    start_date_attr = {"id":"rm-post-start-dp", 
                 "placeholder": "Start Date"}
    end_date_attr = {"id":"rm-post-end-dp", 
                 "placeholder": "Start Date"}

    goal = forms.CharField(widget=forms.Textarea(attrs=goal_attr), required=True)
    start_date = forms.DateField(widget=forms.TextInput(attrs=start_date_attr), required=True)
    end_date = forms.DateField(widget=forms.TextInput(attrs=end_date_attr), required=True)
