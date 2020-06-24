from django.conf.urls import include, url
from rest_framework import routers
from .views import BoastOrRoastViewSet

router = routers.DefaultRouter()
router.register(r'posts', BoastOrRoastViewSet, basename='posts')

urlpatterns = [
    url(r'', include(router.urls))
]