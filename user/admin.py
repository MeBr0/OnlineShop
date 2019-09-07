from django.contrib import admin
from django.contrib.auth.models import User


# unregister and register again model User
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    # return groups of single user (because of Many-To-Many)
    def group(self, user):
        groups = [group.name for group in user.groups.all()]

        return ' '.join(groups)

    group.short_description = 'groups'

    list_display = ('id', 'username', 'first_name', 'last_name', 'group', 'is_superuser', 'password', )
