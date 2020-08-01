from django.conf.urls import url 
from django_rest_api import views 
 
urlpatterns = [ 
    url(r'^api/country$', views.country_list),
    url(r'^api/country/(?P<pk>[0-9]+)$', views.country_detail),
    url(r'^api/state$', views.state_list),
    url(r'^api/state/(?P<pk>[0-9]+)$', views.state_detail),
    url(r'^api/city$', views.city_list),
    url(r'^api/city/(?P<pk>[0-9]+)$', views.city_detail),
    url(r'^api/person$', views.person_list),
    url(r'^person/(?P<country_name>\D+)/', views.search_view),
    url(r'^api/person/(?P<pk>[0-9]+)$', views.person_detail)
]