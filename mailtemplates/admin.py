from django.contrib import admin
from mailtemplates.models import EMailTemplate


class EMailTemplateAdmin(admin.ModelAdmin):
    actions = ['make_published']

    def make_published(self, request, queryset):
        for email in queryset:
            email.send("i.bauer@cuescience.de", {"var": "nabala"})
    make_published.short_description = "send"




admin.site.register(EMailTemplate, EMailTemplateAdmin)