from django import template
from ..models import Enrollment

register = template.Library()

@register.simple_tag
def has_permission(user, permission):
    return user.has_perm(permission)

@register.inclusion_tag("enrollment_list.html")
def show_enrollments():
    course_enrollments = Enrollment.objects.all()
    return {'enrollments': course_enrollments}


@register.filter(name='transform_value')
def transform_value(value):
    if value=='foo':
        return ('bar')
    return value