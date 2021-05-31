from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Cast

class CastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cast
        fields = ('id', 'url', 'name', 'character', 'oneliner', 'episode')