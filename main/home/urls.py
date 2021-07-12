from django.contrib import admin
from django.urls import path, include 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name='home'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_signup/',views.user_create_account,name='user_signup'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('activate_mail/<uid64>/<token>/',views.mail_activation,name='activate_mail'),
    path('dashboard/',views.dashboard,name='dashboard'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
