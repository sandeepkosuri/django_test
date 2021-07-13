from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

class BooksInline(admin.TabularInline):
    model = Book
    fields = ('title',)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        ('Author details',{'fields' : ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))}),
    )
    inlines = [BooksInline]


admin.site.register(Genre)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'language', 'status', 'due_back')
    list_filter = ('status', 'due_back')

admin.site.register(Author, AuthorAdmin)

admin.site.register(Language)




