from django.urls import path, include
from .views import *
from rest_framework import routers
from .api.views import *
#routers --->simple -->crud
#routers --->Default -->crud,auth,authz,help
router=routers.DefaultRouter()
router.register(r'API',TraineeModelViewSet)


urlpatterns=[
    path('APIH/',info),
    path('',include(router.urls)),
    # path('',alltrainees,name='alltrainees'),
    # # path('Add',add,name='tradd'),
    # path('Add',AddtraineeG.as_view(),name='tradd'),
    # # path('Update/<int:id>',update,name='trupdate'),
    # path('Update/<int:id>',Updatetrainee.as_view(),name='trupdate'),
    # path('Delete/<int:id>',deletetr,name='deletetr'),
    # path('API/',Trainee_List_Create.as_view()),
    # path('APIG/',Trainee_List_Create_G.as_view()),
    # path('APIG/<pk>/',Trainee_get_update_delete_G.as_view()),
    # path('API/<int:id>/',Trainee_get_update_delete.as_view()),



]