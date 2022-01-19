from django.urls import path
from django_hosts.resolvers import reverse
from cathedral import views

app_name = 'cathedral'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('basecontact/', views.basecontactView, name='basecontact'),
]