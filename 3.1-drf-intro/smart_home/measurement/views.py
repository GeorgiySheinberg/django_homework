# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView,  ListCreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, \
    MeasurementsSerializer


class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsAPIList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer

