from dataclasses import fields
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from apps.attendance.models import *


# Create your views here.
class DashboardView(LoginRequiredMixin, CreateView):
    template_name = "dashboard/index.html"
    model = AttendanceURLToken
    fields = ()
    success_url = reverse_lazy('attendance:url_list')