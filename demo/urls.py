from pprint import pprint
from rest_framework.routers import DefaultRouter

from demo.views import CommentViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = router.urls
