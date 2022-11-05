from rest_framework import serializers
from readers.models import Reader


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'