"""RosesAndVows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

# from .views import home, LoginView
from django.views.generic import RedirectView

import Coordinator
from .views import home, LoginView, signup, show_profile, PasswordResetTokenView, \
    PasswordResetView, ConfirmEmailView, LogoutView, ChangePasswordView, about_us
# from .views import dashboard_client as dashboard_client
# from .views import dashboard_eo as dashboard_eo
from Client.views import SignupView as client_signupview
# from Applicant.views import ProfileView
# from Coordinator.views import SignupView as coo_signupview
from RosesAndVows import views
from Profile.views import ProfileView
from Post.views import post_list, post_new, search

from account.views import SettingsView, DeleteView

from Coordinator.views import MySite
# from Applicant.views import home
# PasswordResetTokenView,

urlpatterns = [
    url(r'^account/login/profile/posts/$', post_list, name='posts'),
    url(r'^account/login/profile/posts/create/$', post_new, name='post_new'),
    url(r'^account/login/profile/posts/search/', search, name='search'),
    # url(r'^account/login/profile/posts/create/', post_new, name='post_new'),
    # url(r'^account/login/profile/posts/(?P<id>\d+)/', post_list, name='posts'),

    url(r'^account/coordinator/site/(?P<id>\d+)/$', MySite , name='site'),

    url(r'^account/signup/client/$', client_signupview.as_view(), name='client_signup'),
    url(r'^account/login/profile/(?P<id>\d+)/', show_profile, name='account_profile'),
    # url(r'^account/login/dashboard_eo/(?P<id>\d+)/', dashboard_eo, name='dashboard_eo'),
    # url(r'^account/login/dashboard_client/(?P<id>\d+)/', dashboard_client, name='dashboard_client'),
    url(r'^account/login/profile/edit/(?P<id>\d+)/', ProfileView.as_view(), name='edit_profile'),

    # url(r'^account/signup/coordinator/', coo_signupview.as_view(), name='coordinator_signup'),
    url(r'^account/signup/', signup, name='account_signup'),

    url(r'^account/login/', LoginView.as_view(), name='account_login'),
    url(r'^account/logout/', LogoutView.as_view(), name="account_logout"),

    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r'^account/password/reset/', PasswordResetView.as_view(), name='account_password_reset'),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),

    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(),
        name="account_password_reset_token"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    url(r"^delete/$", DeleteView.as_view(), name="account_delete"),
    # url(r'^search/$', searchview.as_view(), name='search'),
    url(r'^aboutus/$', about_us, name='about_us'),
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),

    url(r'^', include('django_private_chat.urls'), name='Chat'),
    url(r'^list/', view=views.UserListView.as_view(), name='show'),
    url(r'^dialogs/account/login/',LoginView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
