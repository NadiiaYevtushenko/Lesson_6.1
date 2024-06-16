from django.contrib import admin
from .models import Choice, Question, ChoiceRate

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ChoiceRate)