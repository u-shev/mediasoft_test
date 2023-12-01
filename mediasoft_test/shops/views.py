from rest_framework import generics


from .filters import IsOpenFilter
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetAPIView(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Street.objects.filter(city__id=city_id)


class ShopListView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IsOpenFilter
