from django.urls import path
from . import views
from .views import CookieTokenRefreshView


urlpatterns = [
    path('google/login/', views.google_login, name='google-login'),
    path('google/callback/', views.google_callback, name='google-callback'),
    path('kakao/login/', views.kakao_login, name='kakao-login'),
    path('kakao/callback/', views.kakao_callback, name='kakao-callback'),
    path("api/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name = 'profile'),
    path('profile/<int:user_id>/update/', views.profile_update, name = 'profile-update'),
    path('profile/<int:user_id>/delete/', views.delete_profile, name = 'delete-profile'),
]