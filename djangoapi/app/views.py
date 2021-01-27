from django.shortcuts import render
from rest_framework import viewsets
from app.models import Course
from app.serilizers import Course_Serilizer
# Create your views here.

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Course_Serilizer
    # print(queryset)
    