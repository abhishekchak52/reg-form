from django.contrib import admin
from django.contrib.auth.models import Group
from .models import member
# Register your models here.

class MemberModelAdmin(admin.ModelAdmin):
    list_display = ['name','course','year','timestamp']
    list_filter = ['year','course']
    search_fields = ['name','course']
    class Meta:
        model = member

admin.site.register(member,MemberModelAdmin)
admin.site.unregister(Group)