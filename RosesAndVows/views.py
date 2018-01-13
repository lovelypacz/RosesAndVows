from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from Profile.models import Profile
from Coordinator.forms import ProfileForm
from .forms import PasswordResetTokenForm, ChangePasswordForm

import account.forms
import account.views


class LoginView(account.views.LoginView):
    template_name = 'login.html'
    form_class = account.forms.LoginEmailForm


class LogoutView(account.views.LogoutView):
    template_name = 'logout.html'


class PasswordResetView(account.views.PasswordResetView):
    template_name = 'password_reset.html'
    template_name_sent = "password_reset_sent.html"


class ConfirmEmailView(account.views.ConfirmEmailView):
    def get_template_names(self):
        return {
            "GET": ["email_confirm.html"],
            "POST": ["email_confirmed.html"],
        }[self.request.method]


class PasswordResetTokenView(account.views.PasswordResetTokenView):
    form_class = PasswordResetTokenForm
    template_name = "password_reset_token.html"
    template_name_fail = "password_reset_token_fail.html"

    def form_valid(self, form):
        global trimmed_email
        for x in range(len(self.get_user().email)):
            c = self.get_user().email[x]
            if c == '@':
                trimmed_email = self.get_user().email[0:x]

        if self.get_user().first_name.lower() in form.cleaned_data['password'].lower():
            # messages.add_message(self.request, messages.ERROR, 'Your password must not be too similar to your first name!')
            form.add_error(None, 'Your password must not be too similar to your first name!')
            return super(PasswordResetTokenView, self).form_invalid(form)

        elif self.get_user().last_name.lower() in form.cleaned_data['password'].lower():
            form.add_error(None, 'Your password must not be too similar to your last name!')
            return super(PasswordResetTokenView, self).form_invalid(form)

        elif self.get_user().email.lower() in form.cleaned_data['password'].lower():
            form.add_error(None, 'Your password must not be too similar to your email address!')
            return super(PasswordResetTokenView, self).form_invalid(form)

        elif trimmed_email.lower() in form.cleaned_data['password'].lower():
            form.add_error(None, 'Your password must not be too similar to your email address!')
            return super(PasswordResetTokenView, self).form_invalid(form)

        else:
            self.change_password(form)
            self.create_password_history(form, self.request.user)
            self.after_change_password()
            return redirect(self.get_success_url())


class ChangePasswordView(account.views.ChangePasswordView):
    form_class = ChangePasswordForm

    def form_valid(self, form):
        global trimmed_email
        for x in range(len(self.get_user().email)):
            c = self.get_user().email[x]
            if c == '@':
                trimmed_email = self.get_user().email[0:x]

        if self.get_user().first_name.lower() in form.cleaned_data['password_new'].lower():
            # messages.add_message(self.request, messages.ERROR, 'Your password must not be too similar to your first name!')
            form.add_error(None, 'Your password must not be too similar to your first name!')
            return super(ChangePasswordView, self).form_invalid(form)

        elif self.get_user().last_name.lower() in form.cleaned_data['password_new'].lower():
            form.add_error(None, 'Your password must not be too similar to your last name!')
            return super(ChangePasswordView, self).form_invalid(form)

        elif self.get_user().email.lower() in form.cleaned_data['password_new'].lower():
            form.add_error(None, 'Your password must not be too similar to your email address!')
            return super(ChangePasswordView, self).form_invalid(form)

        elif trimmed_email.lower() in form.cleaned_data['password_new'].lower():
            form.add_error(None, 'Your password must not be too similar to your email address!')
            return super(ChangePasswordView, self).form_invalid(form)

        else:
            self.change_password(form)
            self.create_password_history(form, self.request.user)
            self.after_change_password()
            return redirect(self.get_success_url())


def home(request):
    form = ProfileForm
    print('Request: {}' .format(request.user))
    if request.user is not None and not request.user.is_anonymous:
        logged = User.objects.get(email=request.user)
        print('Request.user : {}' .format(request.user))
        print('Logged: {}' .format(logged.first_name))
        user_group = Group.objects.get(user=logged.id)
        try:
            user_profile = Profile.objects.get(user_id=request.user.id)
        except Profile.DoesNotExist:
            user_profile= None #User profile has not been created.
        print('Userprofile: {}' .format(user_profile))
        print('Usergroup: {}' .format(user_group.name))
        if user_group.name == "Coordinator" and user_profile is None:
            print('User is a coordinator.')
            return render(request, 'edit_profile.html', {'form':form})
        else:
            return render(request, 'body.html')

    else:
        return render(request, 'body.html')


def signup(request):
    return render(request, 'Client/signup.html')


def coordinator_signup(request):
    return render(request, 'Coordinator/signup.html')


def about_us(request):
    return render(request, 'aboutus.html')


def Root_Signup(request):
    return render(request, 'root_signup.html')


def show_profile(request, id):
    profile = get_object_or_404(User, id=id)
    profile_group_user = Group.objects.get(user=id)
    profile_profile = Profile.objects.get(user_id=id)

    if profile_group_user.name == 'Coordinator':
        return render(request, 'Coordinator/dashboard.html', {'profile': profile, \
                                                              'profile_group_user': profile_group_user, \
                                                              'profile_profile': profile_profile})
    else:
        return render(request, 'Client/dashboard-2.html', {'profile': profile, 'profile_group_user': profile_group_user})


class UserListView(generic.ListView):
    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'list.html'

