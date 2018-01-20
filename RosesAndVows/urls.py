from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.contrib import admin
from .views import home, LoginView, signup, show_profile, PasswordResetTokenView, \
    PasswordResetView, ConfirmEmailView, LogoutView, ChangePasswordView, about_us, Root_Signup, userListView
from Client.views import SignupView as client_signupview
from Coordinator.views import SignupView as coo_signupview
from Profile.views import ProfileView
from Post.views import post_list, post_new, search, post_detail, post_edit
from account.views import SettingsView, DeleteView
from Coordinator.views import MySite


urlpatterns = [

    url(r'^account/login/profile/posts/$', post_list, name='posts'),
    url(r'^account/login/profile/posts/(?P<id>\d+)/$', post_edit, name='post_edit'),
    url(r'^account/login/profile/posts/create/$', post_new, name='post_new'),
    url(r'^account/login/profile/posts/list/search/', search, name='search'),
    url(r'^account/login/profile/posts/info/(?P<id>\d+)/$', post_detail, name='post_detail'),
    url(r'^account/coordinator/site/(?P<id>\d+)/$', MySite , name='site'),
    url(r'^account/signup/$', Root_Signup, name='signup'),
    url(r'^account/signup/client/$', client_signupview.as_view(), name='client_signup'),
    url(r'^account/login/profile/(?P<id>\d+)/', show_profile, name='account_profile'),
    url(r'^account/login/profile/edit/(?P<id>\d+)/', ProfileView.as_view(), name='edit_profile'),
    url(r'^account/signup/coordinator/', coo_signupview.as_view(), name='coordinator_signup'),
    url(r'^account/login/', LoginView.as_view(), name='account_login'),
    url(r'^account/logout/', LogoutView.as_view(), name="account_logout"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r'^account/password/reset/', PasswordResetView.as_view(), name='account_password_reset'),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(),
        name="account_password_reset_token"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    url(r"^delete/$", DeleteView.as_view(), name="account_delete"),
    url(r'^aboutus/$', about_us, name='about_us'),
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),
    url(r'^', include('django_private_chat.urls'), name='Chat'),
    url(r'^list/', userListView, name='show'),

    # url(r'^list/', view=UserListView.as_view(), name='show'),
    url(r'^dialogs/account/login/',LoginView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

