from django.contrib import admin
from .models import Profile


from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('wifi/', self.admin_site.admin_view(self.my_view)),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           something="test",
        )
        return TemplateResponse(request, "wifi.html", context)

admin.site.register(Profile, MyModelAdmin)
# admin.site.register(MyModelAdmin,)/