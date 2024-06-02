from django.urls import path
from .views import index, detail, results, vote

urlpatterns = [
    path('poll-index/', index, name='index'),
    path('detail/<int:question_id>/', detail, name='detail'),
    path('results/', results, name='results'),
    path('question/vote/<int:choice_id>/', vote, name='vote'),
]
