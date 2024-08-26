from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from .endpoints import (
    UserViewSetAPI,
    StudentViewSetAPI,
    TeacherViewSetAPI,
    GroupViewSetAPI,
    SpecializationViewSetAPI,
    TeacherStudentListAPIView
)

router = SimpleRouter()
router.register("user", UserViewSetAPI)
router.register("student", StudentViewSetAPI)
router.register("teacher", TeacherViewSetAPI)
router.register("group", GroupViewSetAPI)
router.register("specialization", SpecializationViewSetAPI)


urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "group/(?P<pk>[^/.]+)/teachers-students/", TeacherStudentListAPIView.as_view()
    ),
]
