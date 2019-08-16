from django.urls import path
from Products import views

app_name = 'Products'
urlpatterns = [
    path('create/', views.products_create_view, name='goods'),
    path('detail/', views.products_detail_view, name='detail'),
    path('account/', views.signup, name='account'),
]