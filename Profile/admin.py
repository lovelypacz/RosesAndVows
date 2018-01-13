from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Group'

    list_display = UserAdmin.list_display + ('group',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
