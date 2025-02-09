from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
    
    @swagger_auto_schema(
        method="get",
        manual_parameters=[
            openapi.Parameter(
                name="numbers",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Comma-separated list of numbers to fetch frequency. Example: 1,2,3",
                requred=True
            )
        ],
        responses={200: "List of numbers with their times sorted by highest times."}
    )
    @action(methods=["GET"], detail=False, url_name="number-frequency", url_path="number-frequency")
    def get_number_frequency(self, request):
        """
        Returns the frequency of provided numbers in DigitalStatistics.
        Expects a list of numbers in the request query parameters: 
        """
        numbers = request.query_params.get("numbers", "")

        try:
            number_list = [int(num.strip()) for num in numbers.split(",")]
        except ValueError:
            return Response({"error": "Invalid number format."}, status=400)
        
        frequency_data = (
            DigitalStatistics.objects.filter(number__in=number_list)
            .values("number", "times")
            .order_by("-times")
        )
        return Response(frequency_data)



