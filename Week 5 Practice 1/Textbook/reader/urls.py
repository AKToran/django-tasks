from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.reader_login, name='login'),
    path('logout/', views.reader_logout, name='logout'),
]
