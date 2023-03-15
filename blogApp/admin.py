from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Opportunity, Event, Project, Resource
from django.utils.text import slugify

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name',)
    list_filter = ('role',)

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'created_date', 'deadline', 'completed_date', 'link', 'owner', 'opportunity_type', 'paid', 'completed', 'location')
    list_filter = ('opportunity_type', 'paid', 'completed')
    search_fields = ('title', 'company', 'location')
    ordering = ('-created_date',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'event_type', 'datetime') #display rows
    list_filter = ('event_type', 'datetime') #filter by this
    search_fields = ('title', 'description')
    ordering = ('datetime',)

    def save_model(self, request, obj, form, change):
        if not obj.slug and obj.title:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    ordering = ('title',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner', 'start_date', 'end_date')
    list_filter = ('category', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    ordering = ('title',)

admin.site.register(Event, EventAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Project, ProjectAdmin)
