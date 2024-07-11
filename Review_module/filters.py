import django_filters
from Review_module.models import Review


class ReviewFilter(django_filters.FilterSet):

    class Meta:
         model = Review
         fields = '__all__'

