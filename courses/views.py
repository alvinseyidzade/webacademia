
from django.shortcuts import render

def courses(request):
    return render(request, 'courses/courses_list.html')