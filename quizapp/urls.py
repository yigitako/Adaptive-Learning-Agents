from django.urls import path
from .views import dynamic_quiz_view

urlpatterns = [
    path('', dynamic_quiz_view, name='dynamic_quiz'),
]
