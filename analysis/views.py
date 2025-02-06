from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from analysis.serializers import DigitalStatisticsSerializer
from analysis.models import DigitalStatistics
from analysis.permissions import DigitalStatisticsPermission
from utils.exception import CustomNotFoundException

class AnalysisViewSet(viewsets.GenericViewSet):
    queryset = DigitalStatistics.objects.all()
    serializer_class = DigitalStatisticsSerializer
    permission_classes = [
        IsAuthenticated,
        DigitalStatisticsPermission
    ]

    def get_serializer_class(self):
        return DigitalStatisticsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        payload = serializer.data
        return Response(payload)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except DigitalStatistics.DoesNotExist:
            raise CustomNotFoundException(detail="Digital statistics not found with the given ID.")
    
