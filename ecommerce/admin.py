from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'price', 'stock')
    search_fields = ('name', 'venue__name')  # Ürün adı ve mekan adı ile arama yapılabilir.
    list_filter = ('venue', 'price')
    ordering = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'total_price', 'get_product_count', 'created_at')
    search_fields = ('user__username', 'status', 'id')
    list_filter = ('status', 'user')
    ordering = ('-created_at',)

    def get_product_count(self, obj):
        return obj.products.count()  # Siparişteki ürün sayısını gösterir
    get_product_count.short_description = 'Number of Products'
