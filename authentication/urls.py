from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name = 'home'),
    path('password_reset/', PasswordResetView.as_view(), name = 'password_reset'),
]

