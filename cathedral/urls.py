from django.urls import path
from django_hosts.resolvers import reverse
from cathedral import views

app_name = 'cathedral'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('parishes/', views.ParishPageView.as_view(), name='parish'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('basecontact/', views.basecontactView, name='basecontact'),
]