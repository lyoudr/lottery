from rest_framework import serializers

from analysis.models import DigitalStatistics

class DigitalStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalStatistics
        fields = '__all__'

