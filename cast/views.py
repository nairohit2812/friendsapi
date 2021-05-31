from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Cast
from . serializers import CastSerializer

# Create your views here.

class CastView(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
