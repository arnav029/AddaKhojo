from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3
    fields = ['image', 'caption', 'order']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ['name', 'type', 'sector', 'is_on_google', 'status', 'photo_count', 'created_at']
    list_filter = ['status', 'type', 'is_on_google', 'sector']
    search_fields = ['name', 'location_text', 'caption']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Identity', {'fields': ['name', 'slug', 'type', 'is_on_google', 'status']}),
        ('Location', {'fields': ['sector', 'location_text', 'lat', 'lng']}),
        ('Info', {'fields': ['timings_text', 'price_text', 'vibe_tag', 'practical_notes']}),
        ('Content', {'fields': ['caption']}),
        ('Meta', {'fields': ['created_at', 'updated_at'], 'classes': ['collapse']}),
    ]

    def photo_count(self, obj):
        return obj.photos.count()
    photo_count.short_description = 'Photos'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['place', 'order', 'caption', 'thumb']
    list_filter = ['place']

    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:48px;border-radius:4px">', obj.image.url)
        return '—'
    thumb.short_description = 'Preview'
