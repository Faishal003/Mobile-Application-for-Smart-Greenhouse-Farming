from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    #path('farm/', FarmView.as_view()),
    path('farma/', FarmaView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('farm/<int:id>/', FarmView.as_view()),
    # path('sensor/', SensorView.as_view()),
    path('sensor/<int:id>/', SensorView.as_view()),
    path('login/', obtain_auth_token),
    path('register/', RegisterView.as_view()),
    path('get_user_id/', views.get_user_id, name='get_user_id'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
]
