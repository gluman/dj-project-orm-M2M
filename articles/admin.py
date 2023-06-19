from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Scope, Relations

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
            if count == 0:
                raise ValidationError('Какая-то ошибка')
            else:
                pass
        return super().clean()



class RelationshipInline(admin.TabularInline):
    model = Relations
    extra = 0
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_display_links = ['title']
    inlines = [RelationshipInline]
@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['topic']
