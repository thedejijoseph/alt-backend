from django.urls import path

from . import views
urlpatterns = [
    path('', views.RootView.as_view()),
    path('register/', views.UserSignup.as_view()),
    path('login/', views.UserLogin.as_view()),
]