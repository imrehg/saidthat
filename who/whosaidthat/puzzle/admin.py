from puzzle.models import Category, Person, Quote
from django.contrib import admin

# Simple admin action
def make_verified(modeladmin, request, queryset):
    queryset.update(verified=True)
    make_verified.short_description = "Mark selected people as verified"

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    ordering = ['name']
    actions = [make_verified]

admin.site.register(Category)
admin.site.register(Person, PersonAdmin)
admin.site.register(Quote)


