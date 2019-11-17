from django.contrib import admin
from LIB_APP.models import Book, Author, Redaction, BookHolder


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_release', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country', 'birth_year')


class RedactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookHolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Redaction, RedactionAdmin)
admin.site.register(BookHolder, BookHolderAdmin)
