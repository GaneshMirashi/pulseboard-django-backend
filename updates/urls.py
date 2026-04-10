from rest_framework.routers import SimpleRouter
from .views import UpdateViewSet

router = SimpleRouter()
router.register(r'', UpdateViewSet, basename='update')

urlpatterns = router.urls