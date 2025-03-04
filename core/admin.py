from django.contrib import admin

from django.contrib import admin
from .models import Lesson, QuizQuestion


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')  # Display lesson title and topic in admin panel
    search_fields = ('title', 'topic')  # Enable search functionality


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "lesson", "correct_option")
    search_fields = ("question_text",)