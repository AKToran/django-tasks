from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.BuyerRegisterView.as_view(), name='register' ),
    path('login/', views.BuyerLoginView.as_view(), name='login' ),
    path('logout/', views.BuyerLogoutView.as_view(), name='logout' ),
    path('profile/', views.profile, name='profile' ),

]