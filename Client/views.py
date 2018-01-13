from django.shortcuts import HttpResponse
from django.contrib.auth.models import Group
from Client.forms import SignupForm

import account.views


def home(request):
    return HttpResponse('Home')


class SignupView(account.views.SignupView):
    template_name = 'Client/signup.html'
    template_name_email_confirmation_sent = 'email_confirmation_sent.html'
    form_class = SignupForm

    def generate_username(self, form):
        username = form.cleaned_data['email']
        return username

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self)

    def create_profile(self, form):
        profile = self.created_user
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.save()
        profile.groups.add(Group.objects.get(name='Client'))
