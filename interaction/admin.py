from django.contrib import admin
from .models import Comment, Notification

# CommentAdmin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at')  # created_at'ı ekleyin

    def created_at(self, obj):
        return obj.created_at  # BaseModel'den alınan created_at alanını döndürün
    created_at.admin_order_field = 'created_at'  # Sıralama için
    created_at.short_description = 'Created At'  # Başlık

# NotificationAdmin
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')  # created_at'ı ekleyin

    def created_at(self, obj):
        return obj.created_at  # BaseModel'den alınan created_at alanını döndürün
    created_at.admin_order_field = 'created_at'  # Sıralama için
    created_at.short_description = 'Created At'  # Başlık

admin.site.register(Comment, CommentAdmin)
admin.site.register(Notification, NotificationAdmin)
