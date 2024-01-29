from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.game_list, name='game_list'),
    path('detail/<int:gid>/', views.game_detail, name='game_detail'),
    # path('detail/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
]