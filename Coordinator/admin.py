from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from Profile.models import Profile
from django.conf.urls import url


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['get_username','business_name', 'get_active_status', 'is_validated', 'has_payed','account_actions']

    def get_username(self, obj):
        return User.objects.get(id=obj.user_id).first_name \
                + ' ' + User.objects.get(id=obj.user_id).last_name

    def get_active_status(self, obj):
        return User.objects.get(id=obj.user_id).is_active
    get_username.short_description = 'Organizer'  # Renames column head
    get_active_status.short_description = 'is_active'  # Renames column head

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<account_id>.+)/validate/$',
                self.admin_site.admin_view(self.process_validate),
                name='account-validate',
            ),
            url(
                r'^(?P<account_id>.+)/deactivate/$',
                self.admin_site.admin_view(self.process_deactivate),
                name='account-deactivate',
            ),
            url(
                r'^(?P<account_id>.+)/activate/$',
                self.admin_site.admin_view(self.process_activate),
                name='account-activate',
            ),
        ]
        return custom_urls + urls

    def account_actions(self, obj):
        user = User.objects.get(id=obj.user_id)
        if user.is_active == 0:
            return format_html(
                '<a class="button" href="{}">Validate</a>&nbsp;'
                '<a class="button" href="{}">Activate</a>',
                reverse('admin:account-validate', args=[obj.user_id]),
                reverse('admin:account-activate', args=[obj.user_id]),
            )
        else:
            return format_html(
                '<a class="button" href="{}">Validate</a>&nbsp;'
                '<a class="button" href="{}">Deactivate</a>',
                reverse('admin:account-validate', args=[obj.user_id]),
                reverse('admin:account-deactivate', args=[obj.user_id]),
            )

    def process_validate(self, request, account_id, *args, **kwargs):
        user_profile = Profile.objects.get(user_id=account_id)
        user_profile.is_validated = 1
        user_profile.save()
        return redirect('/admin/Profile/profile')

    def process_deactivate(self, request, account_id, *args, **kwargs):
        user_profile = User.objects.get(id=account_id)
        user_profile2 = Profile.objects.get(user_id=account_id)
        user_profile.is_active = 0
        user_profile2.has_payed = 0
        user_profile.save()
        user_profile2.save()
        return redirect('/admin/Profile/profile')

    def process_activate(self, request, account_id, *args, **kwargs):
        user_profile = User.objects.get(id=account_id)
        user_profile2 = Profile.objects.get(user_id=account_id)
        user_profile.is_active = 1
        user_profile2.has_payed = 1
        user_profile.save()
        user_profile2.save()
        return redirect('/admin/Profile/profile')

    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

    # Filtering on side - for some reason, this works
    list_filter = ['is_validated', 'has_payed']


admin.site.register(Profile, ProfileAdmin)
