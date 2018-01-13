from django.core import exceptions

import django.contrib.auth.password_validation as validators
import account.forms


class PasswordResetTokenForm(account.forms.PasswordResetTokenForm):
    def clean_password_confirm(self):
        if "password" in self.cleaned_data and "password_confirm" in self.cleaned_data:
            if self.cleaned_data["password"] != self.cleaned_data["password_confirm"]:
                super(PasswordResetTokenForm, self).add_error(None, "Password Mismatch.")
            else:
                try:
                    validators.validate_password(self.cleaned_data['password_confirm'])
                except exceptions.ValidationError as err:
                    super(PasswordResetTokenForm, self).add_error(None, '\n'.join(err.messages))
                return self.cleaned_data["password_confirm"]


class ChangePasswordForm(account.forms.ChangePasswordForm):
    def clean_password_new_confirm(self):
        if "password_new" in self.cleaned_data and "password_new_confirm" in self.cleaned_data:
            if self.cleaned_data["password_new"] != self.cleaned_data["password_new_confirm"]:
                super(ChangePasswordForm, self).add_error(None, "You must type the same password each time.")
        return self.cleaned_data["password_new_confirm"]
