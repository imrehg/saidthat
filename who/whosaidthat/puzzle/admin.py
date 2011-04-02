from puzzle.models import Category, Person, Quote, Puzzle
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Simple admin action
def make_verified(modeladmin, request, queryset):
    queryset.update(verified=True)
    make_verified.short_description = "Mark selected people as verified"

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'screenname']
    ordering = ['name']
    actions = [make_verified]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Quote)
admin.site.register(Puzzle)
