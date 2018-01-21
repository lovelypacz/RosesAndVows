from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.models import Group, User
from Coordinator.forms import SignupForm, ProfileForm


from Profile.models import Profile
from Post.models import Post

import account.views


# Create your views here.s
def home(request):
    return HttpResponse('Home')


def MySite(request, id):
    profile = get_object_or_404(User, id=id)
    profile_group_user = Group.objects.get(user=id)
    try:
        profile_profile = Profile.objects.get(user_id=id)
    except Profile.DoesNotExist:
        profile_profile = None

    posts = list(Post.objects.filter(author=id))
    if profile_profile is not None:
        return render(request, 'Coordinator/mysite.html', {'profile': profile, \
                                                       'profile_group_user': profile_group_user, \
                                                       'profile_profile': profile_profile, \
                                                       'posts': posts})
    else:
        return render(request, 'edit_profile.html', {'form': ProfileForm})


class SignupView(account.views.SignupView):
    template_name = 'Coordinator/signup.html'
    template_name_email_confirmation_sent = 'email_confirmation_sent.html'
    form_class = SignupForm

    def generate_username(self, form):
        username = form.cleaned_data['email']
        return username

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        profile = self.created_user
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.save()
        profile.groups.add(Group.objects.get(name="Coordinator"))
