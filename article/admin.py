from django.contrib import admin
from article.models import Article, Comments, Author, Category


# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['name', 'author', 'text', 'headshot', 'category']
    inlines = [ArticleInline]
    list_filter = ['name']


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name']
    list_filter = ['name']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_filter = ['name']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)