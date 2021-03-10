from django.db import models
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import (
    views, 
    mixins, 
    permissions, 
    viewsets,
    generics
)
from rest_framework.serializers import Serializer

from classroom.models import Class, Subject
from .models import Lecture
from .serializer import LectureSerializer, GetStudentSerializer


class LectureTest(views.APIView):
    def get(self,*args, **kwargs):
        return Response({"data": "lectures working"})

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]

class StudentLecture(views.APIView):

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, *args, **kwargs):
        classes_obj = Class.objects.get(title=self.kwargs.get('level'))
        subject_obj = Subject.objects.get(title=self.kwargs.get('subject'))
        qs = Lecture.objects.get(
            level=classes_obj.pk,
            subject=subject_obj.pk,
            term=self.kwargs.get('term')
        )
        lecture_serializer = GetStudentSerializer(qs)
        return Response(lecture_serializer.data)



