"""
Views for the listings app.

This module contains the API views for travel listings and amenities.
"""

from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, Amenity
from .serializers import ListingSerializer, AmenitySerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for travel listings
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "listing_type",
        "is_available",
        "location",
        "max_guests",
        "bedrooms",
    ]
    search_fields = ["title", "description", "location", "address"]
    ordering_fields = ["price_per_night", "created_at", "bedrooms", "max_guests"]

    @action(detail=False)
    def featured(self, request):
        """Get featured listings"""
        featured = self.get_queryset().filter(is_available=True)[:5]
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)


class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for amenities
    """

    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
