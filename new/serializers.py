from rest_framework import serializers

from .models import NewModel


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewModel
        fields = '__all__'
