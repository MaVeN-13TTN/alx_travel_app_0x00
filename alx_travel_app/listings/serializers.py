# Serializers for listings app

from rest_framework import serializers
from .models import Listing, Booking  # Assuming models will be imported from .models


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"  # Or specify fields like ['id', 'title', 'description']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"  # Or specify fields like ['id', 'listing', 'guest', 'check_in_date']


# Add ReviewSerializer later if needed, based on your models
