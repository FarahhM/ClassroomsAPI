from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .serializers import ClassroomSerializer, DetailSerializer, CreateSerializer

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class= ClassroomSerializer

class DetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class CreateView(CreateAPIView):
    serializer_class = CreateSerializer
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class DeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'