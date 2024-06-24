from django.urls import path
from .views import index, detail, results, vote, get_popular_choices, PollIndex, assign_can_view_results_permission
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('poll-index/', index, name='index'),
    path('poll-index_class/', PollIndex.as_view(), name='cb_index'),
    path('detail/<int:question_id>/', detail, name='detail'),
    path('results/', results, name='results'),
    path('question/vote/<int:choice_id>/', vote, name='vote'),
    path('assign-view-results-permission/', assign_can_view_results_permission, name='assign_permission'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]