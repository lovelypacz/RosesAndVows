from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth import get_user_model
from django.core import exceptions
import django.contrib.auth.password_validation as validators

from Profile.models import Profile

from .models import Post

import account.forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['package_name', 'category', 'description', 'image']

        # title =
