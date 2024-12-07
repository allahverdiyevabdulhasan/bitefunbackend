from django.contrib import admin
from .models import ContentReport

# ContentReport modelinin admin görünümünü özelleştirme
class ContentReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reason', 'status', 'created_at', 'updated_at')  # Görüntülenecek alanlar
    search_fields = ('user__username', 'post__id', 'reason')  # Arama yapılacak alanlar
    list_filter = ('status', 'user')  # Filtreleme seçenekleri
    actions = ['mark_as_resolved', 'mark_as_pending']  # Özel admin aksiyonları

    # Raporu 'resolved' olarak işaretleme işlemi
    def mark_as_resolved(self, request, queryset):
        queryset.update(status='resolved')
    mark_as_resolved.short_description = "Mark selected reports as resolved"

    # Raporu 'pending' olarak işaretleme işlemi
    def mark_as_pending(self, request, queryset):
        queryset.update(status='pending')
    mark_as_pending.short_description = "Mark selected reports as pending"

# ContentReport modelini admin paneline kaydetme
admin.site.register(ContentReport, ContentReportAdmin)
