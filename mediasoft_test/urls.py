from django.contrib import admin
from django.urls import path, re_path
from .shops.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/city/', CityAPIView.as_view()),
    re_path('^api/city/(?P<city_id>.+)/street/$', StreetAPIView.as_view()),
    path('api/shop/', ShopListView.as_view()),
]
