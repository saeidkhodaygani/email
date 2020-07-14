from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _




admin.site.register(Post)

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username','get_id', 'first_name', 'last_name', 'is_staff', 'get_role','last_login')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        #(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    def get_id(self, instance):
        return instance.userprofile.id
    def get_role(self, instance):
        return instance.userprofile.role
    get_role.short_description = 'Role'

    list_select_related = ('userprofile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
