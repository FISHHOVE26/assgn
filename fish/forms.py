from django import forms
from django.contrib.auth.forms import UserCreationForm


class inquire(forms.Form):
    name = forms.CharField(label='name', max_length=100,widget=forms.TextInput(attrs={'class':'form-control','id':'name'}))
    email = forms.EmailField(label='email', max_length=200,widget=forms.EmailInput(attrs={'class':'form-control','id':'email'}))
    memo = forms.CharField( label='inquiry', widget=forms.Textarea(attrs={'class':'form-control','id':'memo'}))
    number = forms.CharField( max_length=20,  widget=forms.TextInput(attrs={'class':'form-control','id':'number'}))




class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

