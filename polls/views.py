from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
from .models import Question, Choice, ChoiceRate
from .utils import get_questions_context
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


User = get_user_model()


@login_required
def index(request):
    return render(request, 'index.html', get_questions_context())


class PollIndex(LoginRequiredMixin, View):
    template_name = 'polls/index.html'

    def get(self, request):
        return render(request, self.template_name,get_questions_context())


def detail(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    if question:
        return HttpResponse(f"Here is the question #{question_id} text: {question.question_text}")
    return HttpResponse(f"You're looking at question #{question_id} which does not exist")


@permission_required("polls.can_view_results")
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


@login_required(login_url='/accounts/login/')
def assign_can_view_results_permission(request):
    message = ''
    # try:
    #     user = User.objects.get(id=user_id)
    # except User.DoesNotExist:
    #     message = 'User with provided ID was not found.'
    #     return render(request, 'assign_perm.html')
    if request.method == "POST":
        selected_users = request.POST.getlist('users')

        content_type = ContentType.objects.get_for_model(Question)

        can_view_results_permission = Permission.objects.filter(
            codename='can_view_results',
            content_type=content_type,
        ).first()
        for user_id in selected_users:
            allowed_user = User.objects.filter(id=user_id).first()
            if allowed_user:
                allowed_user.user_permissions.add(can_view_results_permission)

        restricted_users = User.objects.all().exclude(id__in=selected_users)
        for user in restricted_users:
            user.user_permissions.remove(can_view_results_permission)
        return redirect('assign_permission')

    users = User.objects.all()
    return render(request, 'assign_perm.html', {'users': users})