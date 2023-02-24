from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta(object):
        model = Users
        fields = ("company_name", "mobile_phone", "email", "url", "adres",
                  "name_of_major", "in_stock")