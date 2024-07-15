
from django.urls import path
from .api import PatientApiList, PatientApiDetail, ArztApiList, ArztApiDetail




urlpatterns = [
    path('', PatientApiList.as_view()),
    path('<int:pk>', PatientApiDetail.as_view()),


    # ---------- Arzt

    path('list', ArztApiList.as_view()),
    path('list/<int:pk>', ArztApiDetail.as_view()),


]
