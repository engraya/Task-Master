from django.urls import path
from . import views
from .views import ScheduleCreate, ScheduleList, ScheduleDetail, ScheduleUpdate, ScheduleDelete


urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('createSchedule', ScheduleCreate.as_view(), name="createSchedule"),
    path('listSchedule/', ScheduleList.as_view(), name="listSchedule"),
    path('detailSchedule/<int:pk>/', ScheduleDetail.as_view(), name="detailSchedule"),
    path('updateSchedule/<int:pk>/', ScheduleUpdate.as_view(), name="updateSchedule"),
    path('deleteSchedule/<int:pk>/', ScheduleDelete.as_view(), name="deleteSchedule"),
]
