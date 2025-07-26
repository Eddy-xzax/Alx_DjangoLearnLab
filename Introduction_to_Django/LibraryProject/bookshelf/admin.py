from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publication_year')
	list_filter = ('author', 'publication_year')
	search_fields = ('title', 'author_name')

admin.site.register(Book, BookAdmin)
class CustomUserAdmin(UserAdmin):
    model = Customer
    fieldsets = UserAdmin.fieldsets + (
	(None, {'fields' : ('date_of_birth', 'profile_picture')}),
)


admin.site.register(CustomUser, CustomerUserAdmin)
