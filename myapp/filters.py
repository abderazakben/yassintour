import django_filters

from .models import *


class ActivitiesFiter(django_filters.FilterSet):
    class Meta:
        model = Activities
        fields = ('address', )

class  ExcursiontFilter(django_filters.FilterSet):
        class Meta:
            model = Excursions
            fields = {
                'address_E' : ['icontains'],
            }

          

   
