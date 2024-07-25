from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from .models import User, Student, Teacher, Group, Specialization
from .serializers import (
    UserSerializer,
    StudentSerializer,
    SpecializationSerializer,
    TeacherSerializer,
    GroupSerializer,
    TeacherStudentSerializer
)


class UserViewSetAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSetAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSetAPI(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupViewSetAPI(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SpecializationViewSetAPI(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class TeacherStudentListAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Group.objects.filter(pk=pk)
