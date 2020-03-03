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
from django.db import models
import uuid
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,
                                    )
from django.contrib.auth import get_user_model


# Create your models here.

class Company(models.Model):
    """
    Company model
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class Review(models.Model):
    """
    Review model
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    ip_address = models.GenericIPAddressField()
    date = models.DateTimeField(auto_now_add=True, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reviewer} - {self.company}'

    class Meta:
        # Allow only one review per user per restaurant
        unique_together = [['reviewer', 'company']]
