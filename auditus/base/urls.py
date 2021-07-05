from django.urls import path
from auditus.base import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
