from rest_framework import serializers

from .models import (Review,
                     Company,
                     )
from reviewer.users.serializers import UserSerializer
from .fields import CurrentUserIP


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    reviewer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ip_address = serializers.HiddenField(default=CurrentUserIP())

    class Meta:
        model = Review
        fields = ('title', 'company', 'summary', 'rating', 'reviewer', 'ip_address')
