from rest_framework import serializers
from .models import SuperType



class SuperTypeserializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']