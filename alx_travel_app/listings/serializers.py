from rest_framework import serializers
from .models import Listing, ListingImage, Amenity, ListingAmenity


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["id", "image", "caption"]


class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, read_only=True)
    amenities = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "listing_type",
            "price_per_night",
            "location",
            "address",
            "max_guests",
            "bedrooms",
            "bathrooms",
            "featured_image",
            "is_available",
            "created_at",
            "updated_at",
            "images",
            "amenities",
        ]

    def get_amenities(self, obj):
        amenity_items = ListingAmenity.objects.filter(listing=obj)
        return AmenitySerializer(
            [item.amenity for item in amenity_items], many=True
        ).data
