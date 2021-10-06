from django.urls import path
from django.urls.conf import re_path

from .views import *

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/
    path('members/<slug:membersid>/', members), # http://127.0.0.1:8000/members/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), # http://127.0.0.1:8000/archive/2020
]
