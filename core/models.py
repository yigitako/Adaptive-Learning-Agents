from django.db import models
from django.utils.text import slugify


class Lesson(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Unique lesson title
    slug = models.SlugField(unique=True, blank=True)  # URL-friendly version of the title
    topic = models.CharField(max_length=100)  # The category (e.g., "Geometry")
    content = models.TextField()  # The explanation of the topic
    example_problem = models.TextField(blank=True, null=True)  # Example question

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate a slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)  # Link to a lesson
    question_text = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.CharField(
        max_length=10,
        choices=[("option_1", "A"), ("option_2", "B"), ("option_3", "C"), ("option_4", "D")]
    )

    def __str__(self):
        return self.question_text
