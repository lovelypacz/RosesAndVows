from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth import get_user_model
from django.core import exceptions
from Profile.models import Profile

# from django import forms
# from common.utils import send_email
# from . import errors

import account.forms
import django.contrib.auth.password_validation as validators


class SignupForm(account.forms.SignupForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        self.fields['password_confirm'] = account.forms.PasswordField(label=_("Re-Type Password"), )
        field_order = ['first_name', 'last_name', 'email', 'password', 'password_confirm']
        if not OrderedDict or hasattr(self.fields, 'keyOrder'):
            self.fields.keyOrder = field_order
        else:
            self.fields = OrderedDict((k, self.fields[k]) for k in field_order)

    def clean(self):
        if "password" in self.cleaned_data and "password_confirm" in self.cleaned_data and "email" in self.cleaned_data:

            UserModel = get_user_model()
            fake_user = {
                'first_name': self.cleaned_data['first_name'],
                'last_name': self.cleaned_data['last_name'],
                'email': self.cleaned_data['email']
            }

            if self.cleaned_data["password"] != self.cleaned_data["password_confirm"]:
                raise forms.ValidationError(_("Password Mismatch."))
            else:
                try:
                    validators.validate_password(self.cleaned_data['password_confirm'], UserModel(**fake_user))
                except exceptions.ValidationError as err:
                    raise forms.ValidationError('\n'.join(err.messages))
                return self.cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['business_name', 'description', 'contact_no', ]

    business_name = forms.CharField(max_length=20)
    cover_photo = forms.ImageField()
    business_plate = forms.ImageField()
    business_permit = forms.ImageField()
    address = forms.CharField(max_length=100)
    contact_no = forms.CharField(max_length=20)
    description = forms.Textarea()
