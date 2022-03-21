from django.urls import path

from .views import *

app_name = 'attendance'

urlpatterns = [
    path('', UrlListView.as_view(), name='url_list'),
    path('<str:pk>/', AddAttendanceView.as_view(), name='add_attendance'),
    path('<str:pk>/delete/', DeleteAttendanceUrlAndSheet.as_view(), name='delete_attendance')
    
]