from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from .factories import (ReviewFactory,
                        CompanyFactory,
                        )
from reviewer.users.test.factories import UserFactory
from ..models import Review

fake = Faker()


class TestReviewListTestCase(APITestCase):
    """
    Tests /review list operations.
    """

    def setUp(self):
        self.url = reverse('review-list')

        self.user_a = UserFactory()
        self.review_a = ReviewFactory(reviewer=self.user_a)

        self.user_b = UserFactory()
        self.review_b = ReviewFactory(reviewer=self.user_b)

        # need this to create the auth token for fake user
        self.user_a.save()

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_a.auth_token}')

    def test_get_list_reviews(self):
        """
        Test that the user can only list own reviews
        """
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)
        eq_(Review.objects.count(), 2)
        eq_(response.data["count"], 1)
        eq_(response.data["results"][0]["id"], str(self.review_a.id))


class CreateReviewTestCase(APITestCase):
    """
    Tests /review create operations.
    """

    def setUp(self):
        self.url = reverse('review-list')
        self.company = CompanyFactory()
        self.user = UserFactory()
        # need this to create the auth token for fake user
        self.user.save()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_create_review(self):

        data = {'rating': 5,
                'summary': fake.text(),
                'title': fake.bs(),
                'company': self.company.id,
                }

        response = self.client.post(self.url, data=data)
        eq_(response.status_code, status.HTTP_201_CREATED)

    def test_create_review_invalid_rating(self):

        data = {'rating': 80,
                'summary': fake.text(),
                'title': fake.bs(),
                'company': self.company.id,
                }

        response = self.client.post(self.url, data=data)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_invalid_summary(self):

        data = {'rating': 3,
                'summary': 'a' * 10001,
                'title': fake.bs(),
                'company': self.company.id,
                }

        response = self.client.post(self.url, data=data)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_check_ip_address(self):

        data = {'rating': 3,
                'summary': fake.text(),
                'title': fake.bs(),
                'company': self.company.id,
                }

        TEST_IP_ADDRESS = "10.10.10.10"
        response = self.client.post(self.url, data=data, REMOTE_ADDR=TEST_IP_ADDRESS)

        eq_(response.status_code, status.HTTP_201_CREATED)
        eq_(Review.objects.first().ip_address, TEST_IP_ADDRESS)

    def test_create_review_check_reviwer_user(self):

        data = {'rating': 3,
                'summary': fake.text(),
                'title': fake.bs(),
                'company': self.company.id,
                }

        response = self.client.post(self.url, data=data)

        eq_(response.status_code, status.HTTP_201_CREATED)
        eq_(str(Review.objects.first().reviewer.id), self.user.id)
