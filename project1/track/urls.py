from django.urls import path
from .views import *
from .api import views
urlpatterns=[
    path('', getalltracks,name='tracks'),
    path('New/', addtrack,name='addtrack'),
    path('Update/<int:id>/', updatetrack),
    #endpoints
    path('hw/',views.helloworld),
    path('all', views.getall),
]