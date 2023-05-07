from rest_framework import serializers
from .models import Buyer, SiteAbout, Location


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAbout
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
