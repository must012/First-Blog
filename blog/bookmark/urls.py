from django.urls import path
from .views import *

from .models import Bookmark as bm

urlpatterns =[
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
