from django.urls import path
from .views import *
urlpatterns=[
    path('', getalltracks,name='tracks'),
    path('New/', addtrack,name='addtrack'),
    path('Update/<int:id>/', updatetrack),
]