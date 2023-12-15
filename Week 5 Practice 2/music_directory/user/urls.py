from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup" ),
    path('login/', views.loginView.as_view(), name="login" ),
    path('logout/', views.logoutView.as_view(), name="logout" ),
    
]
