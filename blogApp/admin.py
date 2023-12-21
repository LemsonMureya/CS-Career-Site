from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Opportunity, Event, Project, Resource, BlogPost, Tag
from django.utils.text import slugify

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name',)
    list_filter = ('role',)


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'created_date', 'deadline', 'link', 'owner', 'opportunity_type', 'location', 'salary_min', 'salary_max', 'is_open', 'is_remote')
    list_filter = ('opportunity_type',)
    search_fields = ('title', 'company', 'location')
    ordering = ('-created_date',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'event_type', 'datetime')
    list_filter = ('event_type', 'datetime') 
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

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date', 'category', 'is_approved', 'is_published')
    list_filter = ('category', 'is_approved', 'is_published')
    search_fields = ('title', 'description')
    ordering = ('-created_date',)

    def save_model(self, request, obj, form, change):
        if not obj.slug and obj.title:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Event, EventAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)
