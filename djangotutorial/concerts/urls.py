# concerts/urls.py
from django.urls import path
from .views import concert_list, concert_detail, concert_report, create_concert

urlpatterns = [
    path('', concert_list, name='concert_list'),
    path('concert/<int:concert_id>/', concert_detail, name='concert_detail'),
    path('report/', concert_report, name='concert_report'),
    path('concert/create/', create_concert, name='create_concert'),
]
