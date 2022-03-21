from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ( AdnSignUpView, AdnLoginView)

app_name = 'accounts'

urlpatterns = [
    path('login', AdnLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
