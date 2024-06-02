from .models import Question

def get_questions_context():
     all_questions = Question.objects.all()
     return {'questions': {question: question.choice_set.all() for question in all_questions}}
    # return {'questions': None}