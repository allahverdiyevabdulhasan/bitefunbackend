from django.contrib import admin
from .models import Post, Story, Highlight

# Post modelinin admin görünümünü özelleştirme
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'is_active', 'created_at', 'updated_at')  # Görüntülenecek alanlar
    search_fields = ('user__username', 'content')  # Arama yapılacak alanlar
    list_filter = ('is_active', 'user')  # Filtreleme seçenekleri

# Story modelinin admin görünümünü özelleştirme
class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'expires_at', 'created_at', 'updated_at')  # Görüntülenecek alanlar
    search_fields = ('user__username', 'content')  # Arama yapılacak alanlar
    list_filter = ('user', 'expires_at')  # Filtreleme seçenekleri

# Highlight modelinin admin görünümünü özelleştirme
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('user', 'story', 'title', 'created_at', 'updated_at')  # Görüntülenecek alanlar
    search_fields = ('user__username', 'title')  # Arama yapılacak alanlar
    list_filter = ('user', 'story')  # Filtreleme seçenekleri

# Modelleri admin paneline kaydetme
admin.site.register(Post, PostAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Highlight, HighlightAdmin)
