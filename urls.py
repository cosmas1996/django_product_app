from django.urls import path
from Accounts import views


urlpatterns = [
    path('users/', views.login, name='home'),
    path('', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/profile', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_change'),
    path('user/profile/upload_image', views.profile_image_upload, name='image_upload'),
    path('user/profile/all_images', views.user_images, name='all_images')

]