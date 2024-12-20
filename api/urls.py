from django.urls import path
from api.views import CheckPredictionLock, SensorList, SensorEnergyPrediction

app_name = "api"

urlpatterns = [
    path("sensors/", SensorList.as_view(), name="sensor-list"),
    path(
        "sensors/energy_prediction/",
        SensorEnergyPrediction.as_view(),
        name="sensor-energy-prediction",
    ),
    path(
        "sensors/prediction_status/",
        CheckPredictionLock.as_view(),
        name="prediction-status",
    ),
]
