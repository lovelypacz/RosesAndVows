from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.models import Group, User

from .forms import SignupForm

import account.views


# Create your views here.s
def home(request):
    return HttpResponse('Home')


def MySite(request, id):
    profile = get_object_or_404(User, id=id)
    profile_group_user = Group.objects.get(user=id)
    return render(request, 'Coordinator/mysite.html', {'profile': profile, 'profile_group_user': profile_group_user})
