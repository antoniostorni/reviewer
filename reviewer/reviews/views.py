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
        return Review.objects.filter(reviewer=user)

    def get_serializer_class(self):
        if self.action == "create":
            return ReviewCreateSerializer
        else:
            return ReviewSerializer
