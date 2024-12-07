from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Görüntülenecek alanlar
    list_display = ('username', 'email', 'account_type', 'is_private', 'profile_picture', 'get_followers_count')
    
    # Arama yapılacak alanlar
    search_fields = ('username', 'email', 'biography')
    
    # Filtreleme seçenekleri
    list_filter = ('account_type', 'is_private')
    
    # Sıralama
    ordering = ('username',)
    
    # Kullanıcı takipçi sayısını kolayca görmek için özel bir metod
    def get_followers_count(self, obj):
        return obj.followers.count()
    get_followers_count.short_description = 'Followers Count'
