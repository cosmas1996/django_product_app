from django.urls import path
from Products import views as p

app_name = 'Products'
urlpatterns = [
    path('create/', p.products_create_view, name='create'),
    path('products_update/<int:id>/', p.products_update_view, name='update'),
    path('products/', p.products_detail_view, name='products'),
    path('products_delete/<int:id>', p.products_delete, name='delete'),
    path('detail/goods/<int:id>', p.products_goods_view, name='goods'),
]