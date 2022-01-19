from django.urls import path, include
from stkevins import views

app_name = 'stkevins'

urlpatterns = [
    path('', views.KevinsPageView.as_view(), name='stkevins'),
]