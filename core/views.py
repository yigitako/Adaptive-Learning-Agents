from django.shortcuts import render, get_object_or_404
from .models import Lesson, QuizQuestion


def home(request):
    return render(request, 'home.html')


def lessons(request):
    selected_topic = request.GET.get('topic')

    if selected_topic:
        lessons = Lesson.objects.filter(topic=selected_topic)
    else:
        lessons = Lesson.objects.all()

    topics = list(Lesson.objects.values_list('topic', flat=True).distinct())  # Ensure topics are a list

    print("DEBUG: Topics Available:", topics)
    print("DEBUG: Selected Topic:", selected_topic)
    print("DEBUG: Lessons Retrieved:", list(lessons))  # Print retrieved lessons

    return render(request, 'lessons.html', {'lessons': lessons, 'topics': topics, 'selected_topic': selected_topic})


def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    return render(request, 'lesson_detail.html', {'lesson': lesson})


def faq(request):
    faqs = [
        {"question": "What is Adaptive Learning?",
         "answer": "Adaptive Learning customizes educational content based on the learner's progress."},
        {"question": "How can I access lessons?",
         "answer": "Simply navigate to the 'Lessons' page and choose a topic to begin learning."},
        {"question": "Is this platform free?", "answer": "Yes! Our learning platform is completely free for students."},
        {"question": "Do I need an account to use the platform?",
         "answer": "No, but creating an account allows you to track progress."},
        {"question": "Can I request a new lesson?",
         "answer": "Absolutely! Contact us through the 'Contact' page with your request."}
    ]
    return render(request, 'faq.html', {'faqs': faqs})


def quiz(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    questions = QuizQuestion.objects.filter(lesson=lesson)

    if request.method == "POST":
        user_answers = request.POST
        score = 0
        total_questions = questions.count()

        results = []
        for question in questions:
            selected_option = user_answers.get(str(question.id))
            is_correct = selected_option == question.correct_option
            if is_correct:
                score += 1
            results.append({"question": question, "selected": selected_option, "correct": is_correct})

        return render(request, "quiz_result.html", {
            "lesson": lesson,
            "score": score,
            "total_questions": total_questions,
            "results": results
        })

    return render(request, "quiz.html", {"lesson": lesson, "questions": questions})
