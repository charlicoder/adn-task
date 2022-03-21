from pyexpat import model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.views.generic.base import TemplateView

import secrets
from .models import *


class UrlListView(LoginRequiredMixin, ListView):
    template_name = 'attendance/url-list.html'
    model = AttendanceURLToken


class AddAttendanceView(LoginRequiredMixin, TemplateView):
    template_name = 'attendance/add-attendance.html'

class DeleteAttendanceUrlAndSheet(LoginRequiredMixin, DeleteView):
    template_name = 'attendance/url_confirm_delete.html'
    model = AttendanceURLToken
    success_url = reverse_lazy('attendance:url_list')