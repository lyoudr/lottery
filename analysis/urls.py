from django.urls import path, include
from rest_framework import routers

from analysis import views

urlpatterns = []

router = routers.DefaultRouter()
router.register(r"", views.AnalysisViewSet)
urlpatterns += router.urls
