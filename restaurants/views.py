from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView


from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation
from django.db.models import Q






class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin,CreateView):
    #mixin accomplishes same as @login_required in function based view
    form_class=RestaurantLocationCreateForm
    '''login_url='/login/'#this would override what you put in settings.'''
    template_name='form.html'
    # success_url='/restaurants/'

    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.owner=self.request.user  #self since it is in class
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context=super(RestaurantCreateView, self).get_context_data(*args,**kwargs)
        context['title']='Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    #mixin accomplishes same as @login_required in function based view
    form_class=RestaurantLocationCreateForm
    '''login_url='/login/'#this would override what you put in settings.'''
    template_name='restaurants/detail-update.html'
    # success_url='/restaurants/'

    def get_context_data(self,*args,**kwargs):
        context=super(RestaurantUpdateView, self).get_context_data(*args,**kwargs)
        name=self.get_object().name
        context['title']=f'Update Restaurant:{name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
