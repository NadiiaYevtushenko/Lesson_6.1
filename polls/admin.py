from django.contrib import admin
from .models import (
    Choice,
    Question,
    ChoiceRate,
    Student,
    Course,
    Enrollment
)

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ChoiceRate)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)