from django.contrib import admin
from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "email",
        "phone",
        "last_login",
        "is_active",
    ]

    @admin.display(ordering="full_name")
    def full_name(self, user):
        return f"{user.first_name} {user.last_name}"
