from django.urls import path
from .views import *
urlpatterns=[

    path('', getalltracks),
    path('New/', addtrack),
    path('Update/<int:id>/', updatetrack),
]