from django.shortcuts import render
from .models import Students
def home(request):
	 student_list = Students.objects.all()
	 return render(request, "students/home.html", {"students": student_list})