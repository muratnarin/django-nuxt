from rest_framework.filters import BaseFilterBackend



class SchoolPriceRangeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view=None):
        if "price_range" in request.data:
            range = request.data['price_range']
            queryset = queryset.filter(price__gte=range[0], price__lte=range[1])

        return queryset
