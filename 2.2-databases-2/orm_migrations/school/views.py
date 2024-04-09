from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.order_by('group').prefetch_related('teachers')
    data = {
        'students': students
    }
    return render(request, template, context=data)


