from django.contrib import admin
from .models import Author, Employee, Abilities, Position, Status, Person

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_enrollment')]

#@admin.register(Employee)
#class EmployeeAdmin(admin.ModelAdmin):
#    list_display = ('title', 'author', 'position')
#    list_filter = ('position', 'title')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('employee', 'status', 'borrower')
    fieldsets = (
        ('Personal info', {
            'fields': ('employee', 'passport', 'iin')
        }),
        ('Status', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )

class PersonInline(admin.TabularInline):
    model = Person

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'position')
    inlines = [PersonInline]


# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Employee)
admin.site.register(Abilities)
admin.site.register(Position)
admin.site.register(Status)
# admin.site.register(Person)