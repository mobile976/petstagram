from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from petstagram.accounts.forms import AppUserCreationForm, AppUserChangeForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    """
    AppUser дээр Profile-ийг inline байдлаар харуулах.
    Нэг user = нэг profile (OneToOne) тул can_delete=False байна.
    """
    model = Profile
    can_delete = False
    fk_name = "user"
    extra = 0


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    inlines = [ProfileInline]

    list_display = ("pk", "email", "profile_name", "is_staff", "is_superuser", "is_active")
    search_fields = ("email", "profile__first_name", "profile__last_name")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    ordering = ("pk",)

    readonly_fields = ("last_login",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def profile_name(self, obj):
        """
        Жагсаалт дээр profile-ийн нэр (first+last) эсвэл Anonymous User гэж харагдана.
        """
        try:
            return obj.profile.get_profile_name()
        except Profile.DoesNotExist:
            return "No profile"

    profile_name.short_description = "Profile name"

    def get_inline_instances(self, request, obj=None):
        """
        Шинэ user үүсгэж байхад ProfileInline шууд гарахгүй, 
        зөвхөн байгаа user-ийг засах үед гарна.
        """
        if not obj:
            return []
        return super().get_inline_instances(request, obj)