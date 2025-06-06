from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário", max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Digite seu usuário',
        'class': 'form-control',
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'placeholder': 'Digite sua senha',
        'class': 'form-control',
    }))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Digite seu email',
        'class': 'form-control',
    }))
    username = forms.CharField(label="Usuário", max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Escolha um nome de usuário',
        'class': 'form-control',
    }))
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'placeholder': 'Digite a senha',
        'class': 'form-control',
    }))
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirme a senha',
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está cadastrado.")
        return email
