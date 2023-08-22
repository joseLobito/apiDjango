from rest_framework.routers import DefaultRouter
from categories.api.views import *

router_categories = DefaultRouter()

router_categories.register(prefix='catefories', basename='categories', viewset=CategoryApiViewSet)