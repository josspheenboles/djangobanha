from django.urls import path
from .views import *
from .api.views import *
urlpatterns=[

    path('',alltrainees,name='alltrainees'),
    # path('Add',add,name='tradd'),
    path('Add',AddtraineeG.as_view(),name='tradd'),
    # path('Update/<int:id>',update,name='trupdate'),
    path('Update/<int:id>',Updatetrainee.as_view(),name='trupdate'),
    path('Delete/<int:id>',deletetr,name='deletetr'),
    path('API/',Trainee_List_Create.as_view()),
    path('APIG/',Trainee_List_Create_G.as_view()),
    path('APIG/<pk>/',Trainee_get_update_delete_G.as_view()),
    path('API/<int:id>/',Trainee_get_update_delete.as_view()),


]