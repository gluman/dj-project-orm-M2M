from django.contrib import admin

from articles.models import Article, Scope, Relations

class RelationshipInline(admin.TabularInline):
    model = Relations
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image' ]
    inlines = (RelationshipInline,)
@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['articlescope']
    inlines = (RelationshipInline,)
