from django.urls import path, include

urlpatterns = [

    path('', include('stkevins.urls', namespace='stkevins')),
]