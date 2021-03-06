from django import forms
from django.contrib import admin
from make_mozilla.pages import models


class PageSectionInline(admin.StackedInline):
    model = models.PageSection
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('title', 'poster', 'content',),
        }),
        ('Sidebar', {
            'classes': ('collapse',),
            'fields': ('quotes', 'sidebar',),
        }),
    )
    filter_horizontal = ('quotes',)


class PageAdmin(admin.ModelAdmin):
    inlines = [PageSectionInline]
    prepopulated_fields = {'path': ('title',)}
    list_display = ('title', 'path',)
    fieldsets = (
        (None, {
            'fields': ('title', 'path',),
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('additional_content',),
        }),
    )


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('clean_quote', 'source',)
    list_filter = ('source',)


class QuoteSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'strapline',)


admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Quote, QuoteAdmin)
admin.site.register(models.QuoteSource, QuoteSourceAdmin)
