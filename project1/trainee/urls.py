from django.urls import path
from .views import *
urlpatterns=[

    path('',alltrainees,name='alltrainees'),
    # path('Add',add,name='tradd'),
    path('Add',AddtraineeG.as_view(),name='tradd'),
    # path('Update/<int:id>',update,name='trupdate'),
    path('Update/<int:id>',Updatetrainee.as_view(),name='trupdate'),
    path('Delete/<int:id>',deletetr,name='deletetr'),


]