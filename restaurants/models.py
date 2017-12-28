from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_category
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
# Create your models here.

User=  settings.AUTH_USER_MODEL #do it this way in case we want to customize different than django model

class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self,query):#RestaurantLocation.objects.all().search(query)
        return self.filter(
        Q(name__icontains=query)|
        Q(location__icontains=query)|
        Q(category__icontains=query)|
        Q(item__name__icontains=query)|
        Q(item__contents__icontains=query)
        ).distinct()

class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)
    def search(self,query):#RestaurantLocation.objects.search()
        return self.get_queryset().search(query)


class RestaurantLocation(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=120)
    location        =models.CharField(max_length=120, null=True, blank=True)
    category        =models.CharField(max_length=122, null=True, blank=True, validators=[validate_category])

    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    slug            =models.SlugField(null=True, blank=True)
    #my_date_field   =models.DateTimeField(auto_now=False, auto_now_add=False)
#last field is if you wanted your own customizable field
    objects=RestaurantLocationManager()#adding to Model.objects.all
    def __str__(self):
        return(self.name)

    # def get_absolute_url(self):
    #     return f"/restaurants/{self.slug}"

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug':self.slug})


    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)
    print(instance.slug)
    instance.category=instance.category.capitalize()
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
        #instance.save() don't have to do this because pre save does it
        print(instance.slug)

# def rl_post_save_receiver(sender, instance, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     # if not instance.slug:
#     #     instance.slug=unique_slug_generator(instance)
#     #     instance.save()

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)
