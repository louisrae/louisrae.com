from django.contrib import admin

from .models import BookList, Devlog, EssayPost

# Register your models here.


# Register your models here.


class EssayAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "slug", "create_date")
    search_fields = ["title"]


class DevlogAdmin(admin.ModelAdmin):
    list_display = ("month", "content")
    search_fields = ["content"]


class BookAdmin(admin.ModelAdmin):
    list_display = ("book_title", "author", "read_again", "notes")
    search_fields = ["book_title"]


admin.site.register(EssayPost, EssayAdmin)
admin.site.register(Devlog, DevlogAdmin)
admin.site.register(BookList, BookAdmin)
