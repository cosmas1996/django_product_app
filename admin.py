from django.contrib import admin
from .models import Product
from django.urls import path


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'date_created', 'price']
    search_fields = ['title', 'id']
    list_filter = ['title', 'id']
    list_display_links = ['title']
    list_per_page = 6

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Product admin'
admin.site.site_title = 'Product admin'
admin.site.index_title = 'Product administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path(r'^admin/', admin.site.urls),
]


# Register your models here.
