from django.urls import path
from . import views

urlpatterns = [
    path('publisher/<int:pcid>/', views.publisher_creator_detail, name = 'publisher_detail'),
    path('creator/<int:pcid>/', views.publisher_creator_detail, name = 'creator_detail'),
    path('follow/<int:pcid>/', views.follow_pc, name='follow_pc'),
]