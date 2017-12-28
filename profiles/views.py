from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import Http404
from django.contrib.auth import get_user_model
from restaurants.models import RestaurantLocation
from menus.models import Item
# Create your views here.
User =get_user_model()

class ProfileDetailView(DetailView):
    template_name='profiles/user.html'

    def get_object(self):
        username=self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context=super(ProfileDetailView,self).get_context_data(*args, **kwargs)
        user=context['user']
        query = self.request.GET.get('q').strip()
        item_exists=Item.objects.filter(user=user).exists()
        qs=RestaurantLocation.objects.filter(owner=user)
        if query:
            #qs=RestaurantLocation.objects.search(query)
            qs=qs.search(query)
        if qs.exists() and item_exists:
            context['locations']=qs
        return context