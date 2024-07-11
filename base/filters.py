import django_filters
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
  # field = django_filters.CharFilter(title='test')
    class Meta:
         model = User
        # exclude = ['image']
         fields = '__all__'
