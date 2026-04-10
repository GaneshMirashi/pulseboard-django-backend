from rest_framework.routers import SimpleRouter
from .views import CommentViewSet

router = SimpleRouter()
router.register(r'', CommentViewSet, basename='comment')

urlpatterns = router.urls