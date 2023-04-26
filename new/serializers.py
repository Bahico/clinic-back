from rest_framework import serializers

from account.models import SiteAbout
from .models import NewModel


class NewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        about = SiteAbout.objects.get(id=1)
        about.news += 1
        about.save()
        return NewModel.objects.create(**validated_data)

    class Meta:
        model = NewModel
        fields = '__all__'
