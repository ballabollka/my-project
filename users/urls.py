from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import UserProfileAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('api/user/profile/', UserProfileAPIView.as_view(), name='user-profile'),
]


