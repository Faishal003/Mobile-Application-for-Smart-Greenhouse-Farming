from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class FarmaView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get(self, request):
        farm = Farm.objects.all()
        serializer = FarmSaerializer(farm, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmSaerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



class FarmView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        Farm = self.get_queryset().filter(user_id=kwargs["id"])
        if not Farm.exists():
            return JsonResponse({"message": "farm not found"}, status=404)

        Farm_data = []

        for Farm in Farm:
            serialized_Farm = self.get_serializer(Farm)
            Farm_data.append(serialized_Farm.data)

        return JsonResponse(Farm_data, safe=False, status=200)
    


# class FarmView(APIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     def get(self, request):
#         farm = Farm.objects.all()
#         serializer = FarmSerializer(farm, many=True)
#         return Response(serializer.data)
    

#     def post(self, request):
#         serializer = FarmSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

# class SensorView(APIView):
#     def get(self, request):
#         sensor = SensorTable.objects.all()
#         serializer = SensorTableSerializer(sensor, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SensorTableSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

class SensorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorTable.objects.all()
    serializer_class = SensorTableSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        sensor = self.get_queryset().filter(farm_id=kwargs["id"])

        if not sensor.exists():
            return JsonResponse({"message": "Sensor not found"}, status=404)

        sensor_data = []

        for sensor in sensor:
            serialized_sensor = self.get_serializer(sensor)
            sensor_data.append(serialized_sensor.data)

        return JsonResponse(sensor_data, safe=False, status=200)
    

class RegisterView(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response({"error": True})
    


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_id(request):
    user_id = request.user.id
    return Response({'user_id': user_id}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user_info(request):
    user = request.user
    user_info = {
        "username": user.username,
        "user_id": user.id
    }
    return Response(user_info)



class SensorsView(APIView):
    def get(self, request):
        sensor = SensorTable.objects.all()
        serializer = SensorTableSerializer(sensor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorTableSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)