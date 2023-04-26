from rest_framework import serializers

from account.models import SiteAbout
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        about = SiteAbout.objects.get(id=1)
        about.products += 1
        about.save()
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = '__all__'
