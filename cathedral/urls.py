from django.urls import path
from django_hosts.resolvers import reverse
from cathedral import views

app_name = 'cathedral'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    #path('test/', views.TestPageView.as_view(), name='test'),

    path('reflections/', views.ReflectionListView.as_view(), name='reflection_list'),
    path('reflections/<int:year>/<int:month>/<int:day>/<slug:reflection>/', views.reflection_detail, name='reflection_detail'),

    path('parishes/', views.ParishPageView.as_view(), name='parish'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('basecontact/', views.basecontactView, name='basecontact'),
]