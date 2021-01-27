from rest_framework import serializers
from app.models import Course

class Course_Serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields='__all__'    #hyperlinked used to navigate individual
    