from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea


class AddPostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш E-mail'}))
    number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Оставьте ваше сообщение'}))


class RegisterForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш E-mail'}))
    number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    text = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            })}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

        # class AuthUserForm(AuthenticationForm, forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
# fields = ['title', 'anons', 'full_text', 'date']
# widgets = {
#     'title': forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Название статьи'
#     }),
#     'anons': forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Анонс статьи'
#     }),
#     'date': forms.DateTimeInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Дата публикации'
#     }),
#     'full_text': forms.Textarea(attrs={
#         'class': 'form-control',
#         'placeholder': 'Текст статьи'
#     }),
#
# }
