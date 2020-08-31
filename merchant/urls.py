from django.urls import path

from . import views
urlpatterns = [
    path('', views.RootView.as_view())
]