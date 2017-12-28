
from django.conf.urls import url

from .views import (RestaurantListView,RestaurantDetailView,RestaurantCreateView,RestaurantUpdateView,#restaurant_createview
# SearchRestaurantListView,
# ItalianRestaurantListView, JapaneseRestaurantListView, MexicanRestaurantListView,

)
#restaurant_listview,HomeView,AboutView,ContactTemplateView






urlpatterns = [


    url(r'^create/$', RestaurantCreateView.as_view(),name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(),name='edit'),
    # url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'$', RestaurantListView.as_view(),name='list'),

]
