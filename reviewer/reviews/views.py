from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Review
from .serializers import (ReviewSerializer,
                          ReviewCreateSerializer,
                          )


class ReviewView(generics.ListAPIView,
                 generics.CreateAPIView,
                 viewsets.GenericViewSet):

    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the reviews
        for the currently authenticated user.
        """
        user = self.request.user
        return Review.objects.filter(reviewer=user).order_by('date')

    def get_serializer_class(self):
        if self.action == "create":
            return ReviewCreateSerializer
        else:
            return ReviewSerializer
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
