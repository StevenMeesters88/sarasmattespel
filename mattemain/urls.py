from django.urls import path, include
from .views import index, correct, wrong, re_start


urlpatterns = [
    path('', index, name='index'),
    path('wrong/', wrong, name='wrong'),
    path('correct/', correct, name='correct'),
    path('re_start/', re_start, name='re_start')
]
