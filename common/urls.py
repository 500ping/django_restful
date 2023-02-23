from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet
from snippets.views import SnippetViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'snippets', SnippetViewSet, basename="snippet")

urlpatterns = [
    path('', include(router.urls)),
]
