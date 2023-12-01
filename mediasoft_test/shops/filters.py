from django_filters import rest_framework as filters
from .models import Shop
import datetime


class IsOpenFilter(filters.FilterSet):
    open = filters.NumberFilter(field_name='open', method='is_open')

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def is_open(self, queryset, field_name, value):
        queryset = Shop.objects.all()

        open_status = self.request.GET.get('open')
        street = self.request.GET.get('street')
        city = self.request.GET.get('city')

        if street:
            queryset = queryset.filter(street=street)
        if city:
            queryset = queryset.filter(city=city)
        if open_status is not None:
            current_time = datetime.datetime.now().time()
            if open_status == '0':
                queryset = queryset.filter(closing_time__lt=current_time)
            elif open_status == '1':
                queryset = queryset.filter(opening_time__lte=current_time,
                                           closing_time__gt=current_time)
        return queryset
