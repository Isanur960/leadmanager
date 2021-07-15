from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()

router.register(prefix= 'api/leads', viewset = LeadViewSet, basename='leads')

urlpatterns = router.urls