from django.urls import path
from .views import index, detail, results, vote, get_popular_choices

urlpatterns = [
    path('poll-index/', index, name='index'),
    path('detail/<int:question_id>/', detail, name='detail'),
    path('results/', results, name='results'),
    path('question/vote/<int:choice_id>/', vote, name='vote'),
    path('get-popular-choices/', get_popular_choices, name='get_popular_choices'),
]
