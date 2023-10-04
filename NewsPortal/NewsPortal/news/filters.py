from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import *
from django.forms import DateTimeInput

class FilterPost(FilterSet):
    postCategory = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категории',
    )

    filter_date = DateTimeFilter(
        field_name='dateCreate',
        lookup_expr='lt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }