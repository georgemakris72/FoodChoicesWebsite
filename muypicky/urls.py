"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from restaurants.views import (RestaurantListView,RestaurantDetailView,RestaurantCreateView,restaurant_createview
# SearchRestaurantListView,
# ItalianRestaurantListView, JapaneseRestaurantListView, MexicanRestaurantListView,

# )
#restaurant_listview,HomeView,AboutView,ContactTemplateView


from django.views.generic import TemplateView
 #ContactView no longer importing contact or ContactView, or home, or about

# from django.contrib.auth import views as auth_views
#
# path('accounts/login/', auth_views.LoginView.as_view()),

from django.contrib.auth.views import LoginView, PasswordResetView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', home),
    # url(r'^about/$', about),
    url(r'^$', TemplateView.as_view(template_name='home.html'),name='home'),
    # url(r'^restaurants/$', restaurant_listview),

    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),

    # url(r'^restaurants/$', RestaurantListView.as_view(),name='restaurants'),
    # url(r'^restaurants/italian$', ItalianRestaurantListView.as_view()),
    # url(r'^restaurants/japanese$', JapaneseRestaurantListView.as_view()),
    # url(r'^restaurants/mexican$', MexicanRestaurantListView.as_view()),
    # url(r'^restaurants/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
    # url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
    # url(r'^restaurants/create/$', restaurant_createview),
    # url(r'^restaurants/create/$', RestaurantCreateView.as_view(),name='restaurants-create'),
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),
    # SearchRestaurantListView,),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),name='about'),
    # url(r'^contact$', contact),
    #url(r'^contact/$', ContactView.as_view()), #do as view to create instance of class
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),


]
