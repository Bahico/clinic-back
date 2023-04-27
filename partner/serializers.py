from rest_framework import serializers

from partner.models import PartnerModel


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerModel
        fields = '__all__'
