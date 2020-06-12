from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Course

def index(request):
  course_list = Course.objects.all()
  return render(request, 'courses/index.html', {'course_list': course_list })

def detail(request, slug):
  course = get_object_or_404(Course, slug=slug)
  return render(request, 'courses/detail.html',{'course': course})