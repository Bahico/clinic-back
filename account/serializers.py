from rest_framework import serializers
from .models import Buyer, SiteAbout


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAbout
        fields = '__all__'
