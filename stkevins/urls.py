from django.urls import path, include
from stkevins import views

app_name = 'stkevins'

urlpatterns = [
    path('', views.KevinsPageView.as_view(), name='stkevins'),

    path('calender/', views.EventListView.as_view(), name='event_list'),
    path('calender/<int:year>/<int:month>/<int:day>/<slug:event>/', views.event_detail, name='event_detail'),

    path('sacraments/', views.SacramentListView.as_view(), name='sacrament_list'),
    path('sacraments/<slug:slug>/', views.SacramentDetailView.as_view(), name='sacrament_detail'),

    path('communities/', views.CommunityListView.as_view(), name='community_list'),
    path('communities/<slug:slug>/', views.CommunityDetailView.as_view(), name='community_detail'),

    path('societies/', views.SocietyListView.as_view(), name='society_list'),
    path('societies/<slug:slug>/', views.SocietyDetailView.as_view(), name='society_detail'),

    path('parishioners/', views.ParishionerListView.as_view(), name='parishioner_list'),
    path('parishioner/<slug:slug>/', views.ParishionerDetailView.as_view(), name='parishioner_detail'),

    path('history/', views.HistoryPageView.as_view(), name='history'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),

]