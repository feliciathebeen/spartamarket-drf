from django.urls import path
from .views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('signup/', UserView.as_view(), name='signup'),
    path("delete/<int:pk>", UserView.as_view(), name="delete"),
    path("profile/<int:pk>/", UserView.as_view(), name="profile"),
]



