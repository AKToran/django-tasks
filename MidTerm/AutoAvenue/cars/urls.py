from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>', views.CarDetailsView.as_view(), name='details'),
    path('buy/<int:id>', views.BuyCar, name='buy'),

]