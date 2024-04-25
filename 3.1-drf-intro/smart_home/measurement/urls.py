from django.urls import path

from measurement.views import SensorAPIList, SensorAPIUpdate, MeasurementsAPIList

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPIList.as_view()),
    path('sensors/<int:pk>/', SensorAPIUpdate.as_view()),
    path('measurements/', MeasurementsAPIList.as_view()),
]
