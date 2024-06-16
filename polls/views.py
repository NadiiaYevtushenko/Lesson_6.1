from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
from .models import Question, Choice, ChoiceRate
from .utils import get_questions_context


def index(request):
    return render(request, 'index.html', get_questions_context())


def detail(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    if question:
        return HttpResponse(f"Here is the question #{question_id} text: {question.question_text}")
    return HttpResponse(f"You're looking at question #{question_id} which does not exist")


def results(request):
    return render(request, 'results.html', get_questions_context())


def vote(request, choice_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    choice = Choice.objects.filter(id=choice_id).first()
    if choice:
        choice.vote()
    return redirect('index')


def get_popular_choices(request):
    if request.method == "POST":
        if search_string:=request.POST['search']:
            choice_rate = ChoiceRate.objects.first().choice_rate

            search_result = Choice.objects.filter(
                Q(choice_text__icontains=search_string) &
                Q(votes__gte=choice_rate or 0)
            )
            return render(request, 'popular_choices.html', {'search_result': search_result})
    return render(request, 'popular_choices.html')

