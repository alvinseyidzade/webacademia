
from django.shortcuts import render
from courses.models import Category, Course

def home(request):
    categories = Category.objects.all()
    courses = Course.objects.all().order_by('-purchased')
    return render(request, 'home/index.html', {'categories': categories, 'courses': courses})
