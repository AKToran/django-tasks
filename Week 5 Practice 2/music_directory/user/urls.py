from django.urls import path
from . import views

urlpatterns = [
    path('user/signup/', views.SignupView.as_view(), name="signup" ),
    path('user/login/', views.loginView.as_view(), name="login" ),
    path('user/logout/', views.logoutView.as_view(), name="logout" ),
    
]
