from django.contrib import admin

from .models import Article, Scope, Tag

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if not form.cleaned_data:
                continue
            if form.cleaned_data['is_main']:
                main_count += 1
            if main_count > 1:
                raise ValidationError('Основной раздел может быть только один')
        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleInline(admin.TabularInline):
    model = Article.tags.through
    formset = ArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'published_at')


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag', 'is_main')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
