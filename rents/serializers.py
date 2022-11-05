from rest_framework import serializers
from rents.models import Rent


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'