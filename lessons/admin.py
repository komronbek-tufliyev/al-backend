from django.contrib import admin
from .models import (
    Book,
    Archive,
    BookImage,
    ArchiveImage,
    Topic,
    TopicImage,
)

class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1

class ArchiveImageInline(admin.TabularInline):
    model = ArchiveImage
    extra = 1

class TopicImageInline(admin.TabularInline):
    model = TopicImage
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookImageInline]
    list_display = ['title', 'category', 'author', 'publisher']
    list_filter = ['category', 'author', 'publisher']

class ArchiveAdmin(admin.ModelAdmin):
    inlines = [ArchiveImageInline]
    list_display = ['title', 'category', 'author', 'publisher']
    list_filter = ['category', 'author', 'publisher']

class TopicAdmin(admin.ModelAdmin):
    inlines = [TopicImageInline]
    list_display = ['title', 'category', 'author',]
    list_filter = ['category', 'author', ]

admin.site.register(Book, BookAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Topic, TopicAdmin)