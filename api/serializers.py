from rest_framework import serializers
from classes.models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year',]

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields= '__all__'

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year',]

