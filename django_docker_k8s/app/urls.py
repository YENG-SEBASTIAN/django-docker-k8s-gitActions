
from django.urls import path
from app.views import HelloView

urlpatterns = [
    path('', HelloView.as_view()),
]