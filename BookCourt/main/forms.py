from .models import Users
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, URLInput, NumberInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["company_name", "mobile_phone", "email", "url", "adres",
                  "name_of_major", "password"]

        widgets = {
            "company_name": TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Название компании',
                'required': 'required'
            }),
            "mobile_phone": TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Телефон',
                'required': 'required'
            }),
            "email": EmailInput(attrs={
                'class': 'form-field',
                'placeholder': 'Email',
                'required': 'required'
            }),
            "url": URLInput(attrs={
                'class': 'form-field',
                'placeholder': 'Ссылка на сайт',
                'required': 'required'
            }),
            "adres": TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Адрес',
                'required': 'required'
            }),
            "name_of_major": TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Представитель (ФИО)',
                'required': 'required'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-field',
                'placeholder': 'Пароль',
                'required': 'required'
            })
        }















