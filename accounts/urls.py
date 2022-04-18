from django import views
from django.urls import path
from accounts.views import SignUpView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    # path('register', views.register, name='register'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
]