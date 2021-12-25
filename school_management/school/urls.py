from rest_framework.routers import SimpleRouter
from school.views import SchoolViewSet, StudentViewSet

router = SimpleRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
