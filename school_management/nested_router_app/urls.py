from django.urls import path, include
from rest_framework_nested import routers
from nested_router_app.views import SchoolViewSet, StudentViewSet

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)

student_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
student_router.register(r'students', StudentViewSet, basename='school-students')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(student_router.urls)),
]
