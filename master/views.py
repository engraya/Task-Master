from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.

class ScheduleCreate(CreateView):
    model = ScheduleModel
    fields = '__all__'
    template_name = 'master/createSchedule.html'
    success_url = "listSchedule"

class ScheduleList(ListView):
    model = ScheduleModel
    template_name = 'master/listSchedule.html'
    context_object_name = 'schedule'


class ScheduleDetail(DetailView):
    model = ScheduleModel
    template_name = 'master/detailSchedule.html'
    context_object_name = 'schedule'


class ScheduleUpdate(UpdateView):
    model = ScheduleModel
    fields = '__all__'
    template_name = 'master/updateSchedule.html'
    success_url = "/listSchedule"


class ScheduleDelete(DeleteView):
    model = ScheduleModel
    context_object_name = 'schedule'
    template_name = 'master/deleteSchedule.html'
    success_url = "/listSchedule"














def landingPage(request):
    return render(request, 'master/landingPage.html')

def schedulesPage(request):
    return render(request, 'master/schedulesPage.html')



