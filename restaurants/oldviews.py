from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# Create your views here.
# def home_old(request):
#     html_var='f strings'
#     html_=f"""<!DOCTYPE html>
#     <html>
#       <head>
#         <meta charset="utf-8">
#         <title></title>
#       </head>
#       <body>
#         <h1>Hello World!</h1>
#         <p>This is {html_var} coming through</p>
#       </body>
#     </html>"""
#
#     # f strings
#     return HttpResponse(html_)

# def home(request):
#     num=random.randint(0,1000000000)
#     some_list=[num,random.randint(0,1000000000),random.randint(0,1000000000)]
#     context={'html_var':'george',
#             'bool_item':False,
#             'num':num,
#             'some_list':some_list}
#
#     return render(request, "home.html", context)
# #
# def about(request):
#     context={}
#
#     return render(request, "about.html", context)
#
# def contact(request):
#     context={}
#
#     return render(request, "contact.html", context)


# class ContactView(View):
#     def get(self,request,*args,**kwargs):
#         context={}
#         return render(request, "contact.html", context)



# class HomeView(TemplateView):
#     template_name='home.html'
#
#
#     def get_context_data(self, *args, **kwargs):
#         context=super(HomeView,self).get_context_data(*args,**kwargs)
#         num=random.randint(0,1000000000)
#         some_list=[num,random.randint(0,1000000000),random.randint(0,1000000000)]
#         context={'html_var':'george',
#                 'bool_item':False,
#                 'num':num,
#                 'some_list':some_list}
#         return context

# class AboutView(TemplateView):
#     template_name='about.html'
#
#
# class ContactTemplateView(TemplateView):
#     template_name='contact.html'


from .models import RestaurantLocation
from django.db.models import Q

# def restaurant_listview(request):
#     template_name='restaurants/restaurants_list.html'
#     queryset=RestaurantLocation.objects.all()
#     context={'object_list':queryset}
#     return render(request, template_name, context)

# class RestaurantListView(ListView):
#     queryset=RestaurantLocation.objects.all()
#     template_name='restaurants/restaurants_list.html'

# class ItalianRestaurantListView(ListView):
#     queryset=RestaurantLocation.objects.filter(category__iexact='italian')
#     template_name='restaurants/restaurants_list.html'
#
# class JapaneseRestaurantListView(ListView):
#     queryset=RestaurantLocation.objects.filter(category__iexact='japanese')
#     template_name='restaurants/restaurants_list.html'
#
# class MexicanRestaurantListView(ListView):
#     queryset=RestaurantLocation.objects.filter(category__iexact='mexican')
#     template_name='restaurants/restaurants_list.html'

# class SearchRestaurantListView(ListView):
#     template_name='restaurants/restaurants_list.html'
#
#     def get_queryset(self):
#         print(self.kwargs)
#         slug=self.kwargs.get("slug")
#         # if slug:
#         #     queryset=RestaurantLocation.objects.filter(category__icontains=slug)
#         # or use q lookup
#         if slug:
#             queryset=RestaurantLocation.objects.filter(
#             Q(category__iexact=slug)|
#             Q(category__icontains=slug)
#             )
#         else:
#             queryset=RestaurantLocation.objects.none()
#         return queryset

class RestaurantListView(ListView):
    # template_name='restaurants/restaurants_list.html'
    # or could have no template name and will default to what model gives it which is restaurantlocation.html which is what I will do
    def get_queryset(self):
        print(self.kwargs)
        slug=self.kwargs.get("slug")
        print(slug)
        # if slug:
        #     queryset=RestaurantLocation.objects.filter(category__icontains=slug)
        # or use q lookup
        if slug:
            queryset=RestaurantLocation.objects.filter(
            Q(category__iexact=slug)|
            Q(category__icontains=slug)
            )
        else:
            queryset=RestaurantLocation.objects.all()
            print(queryset)
        return queryset


class RestaurantDetailView(DetailView):
    queryset=RestaurantLocation.objects.all()
    # or could have no template name and will default to what model gives it which is restaurantlocation.html
    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context=super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id=self.kwargs.get('rest_id')
    #     obj=get_object_or_404(RestaurantLocation, id=rest_id)#pk=rest_id
    #     return obj


from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

# def restaurant_createview(request):
#     # print(request.GET)
#     # print(request.POST)
#     # form=RestaurantCreateForm()
#     form=RestaurantLocationCreateForm(request.POST or None)
#     errors=None
#         # title=request.POST.get('title')#or request.POST['title'], because it is a dictionary
#         # location=request.POST.get('location')
#         # category=request.POST.get('category')
#         # obj=RestaurantLocation.objects.create(
#         # name=title,
#         # location=location,
#         # category=category
#         # )
#     # if request.method=="POST":
#     #     form=RestaurantCreateForm(request.POST)
#     if form.is_valid():
#         form.save()
#         #.create avoids having to save
#         # obj=RestaurantLocation.objects.create(
#         #         name=form.cleaned_data.get('name'),
#         #         location=form.cleaned_data.get('location'),
#         #         category=form.cleaned_data.get('category')
#         #     )
#         return HttpResponseRedirect('/restaurants')
#     if form.errors:
#         # print(form.errors)
#         errors=form.errors
#
#
#     template_name='restaurants/form.html'
#     context={"form":form, "errors":errors}
#     return render(request, template_name, context)


# def restaurant_createview(request):
#     # print(request.GET)
#     # print(request.POST)
#     # form=RestaurantCreateForm()
#     form=RestaurantCreateForm(request.POST or None)
#     errors=None
#         # title=request.POST.get('title')#or request.POST['title'], because it is a dictionary
#         # location=request.POST.get('location')
#         # category=request.POST.get('category')
#         # obj=RestaurantLocation.objects.create(
#         # name=title,
#         # location=location,
#         # category=category
#         # )
#     # if request.method=="POST":
#     #     form=RestaurantCreateForm(request.POST)
#     if form.is_valid():
#         #.create avoids having to save
#         obj=RestaurantLocation.objects.create(
#                 name=form.cleaned_data.get('name'),
#                 location=form.cleaned_data.get('location'),
#                 category=form.cleaned_data.get('category')
#             )
#         return HttpResponseRedirect('/restaurants')
#     if form.errors:
#         # print(form.errors)
#         errors=form.errors
#
#
#     template_name='restaurants/form.html'
#     context={"form":form, "errors":errors}
#     return render(request, template_name, context)


class RestaurantCreateView(CreateView):
    form_class=RestaurantLocationCreateForm
    template_name='restaurants/form.html'
    success_url='/restaurants/'

@login_required
#could also do this way: @login_required(login_url='/login/')

def restaurant_createview(request):
    form=RestaurantLocationCreateForm(request.POST or None)
    errors=None
    if form.is_valid():
        if request.user.is_authenticated():
            instance=form.save(commit=False)
            instance.owner=request.user
            instance.save()
            return HttpResponseRedirect('/restaurants')
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors=form.errors

    template_name='restaurants/form.html'
    context={"form":form, "errors":errors}
    return render(request, template_name, context)

class RestaurantListView(ListView):

    def get_queryset(self):
        print(self.kwargs)
        slug=self.kwargs.get("slug")
        print(slug)
        if slug:
            queryset=RestaurantLocation.objects.filter(
            Q(category__iexact=slug)|
            Q(category__icontains=slug)
            )
        else:
            queryset=RestaurantLocation.objects.all()
            print(queryset)
        return queryset
