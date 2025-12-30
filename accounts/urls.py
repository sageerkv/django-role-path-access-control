from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('teams/', TeamListView.as_view()),
    path('teams/create/', TeamCreateView.as_view()),
    path('teams/<int:team_id>/update/', TeamUpdateView.as_view()),
    path('teams/<int:team_id>/delete/', TeamDeleteView.as_view()),
]
