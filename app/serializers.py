from rest_framework import serializers
from .models import Special, Testimonial

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ('id', 'name', 'price', 'description')

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ('id', 'name', 'rating', 'description')