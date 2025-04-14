from django.urls import path
from .views import home, lessons, lesson_detail,faq, quiz

urlpatterns = [
    path('', home, name='home'),
    path('lessons/', lessons, name='lessons'),
    path('lesson/<slug:slug>/', lesson_detail, name='lesson_detail'),
    path('faq/', faq, name='faq'),
]