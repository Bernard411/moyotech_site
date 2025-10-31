# your_app/admin.py
from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'role_group', 'order')
    list_editable = ('order',)
    list_filter = ('role_group',)
    search_fields = ('name', 'title')
    
# your_app/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'price', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'tagline', 'short_description')
    prepopulated_fields = {"popup_title": ("name",)}
    
# your_app/admin.py
from django.contrib import admin
from .models import SoftwareProduct, Course, HostingPackage


@admin.register(SoftwareProduct)
class SoftwareProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'price', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'tagline')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'duration', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'subtitle')
    prepopulated_fields = {"popup_title": ("title",)}


@admin.register(HostingPackage)
class HostingPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular', 'order')
    list_editable = ('order', 'is_popular')
    search_fields = ('name',)