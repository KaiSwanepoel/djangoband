from django.urls import path
from . import views

# Page urls
app_name = 'band'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('songs/', views.songs, name='songs'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]