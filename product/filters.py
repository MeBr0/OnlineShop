from django_filters import rest_framework as filters
from order.models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    min_cost = filters.NumberFilter(field_name='cost', lookup_expr='gte')
    max_cost = filters.NumberFilter(field_name='cost', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('name', 'cost',)
