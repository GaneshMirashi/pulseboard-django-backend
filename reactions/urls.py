from rest_framework.routers import SimpleRouter
from .views import ReactionViewSet

router = SimpleRouter()
router.register(r'', ReactionViewSet, basename='reaction')

urlpatterns = router.urls