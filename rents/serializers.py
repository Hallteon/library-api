from rest_framework import serializers
from rents.models import Rent


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ['book', 'book_reader', 'period', 'fine_size']