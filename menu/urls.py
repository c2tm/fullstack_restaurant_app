from django.urls import path

from .views import MenuListAPIView

app_name = 'menu'

urlpatterns = [
    path('', MenuListAPIView.as_view()),
]