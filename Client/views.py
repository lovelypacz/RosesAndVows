from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import Group

from .forms import SignupForm

import account.views
import re

# Create your views here.s
def home(request):
    return HttpResponse('Home')


class SignupView(account.views.SignupView):
    template_name = 'Client/signup.html'
    template_name_email_confirmation_sent = 'email_confirmation_sent.html'
    form_class = SignupForm

    def generate_username(self, form):
        username = form.cleaned_data['email']
        return username

    #Save the email as the username without the extension
    # def generate_username(self, form):
    #     username_1 = form.cleaned_data['email']
    #     username = re.findall('([^@]+)', username_1)
    #     return username[0]

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self)

    def create_profile(self, form):
        profile = self.created_user
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.save()
        profile.groups.add(Group.objects.get(name='Client'))
