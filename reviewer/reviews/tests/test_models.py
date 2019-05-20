from nose.tools import eq_
from rest_framework.test import APITestCase
from .factories import (ReviewFactory,
                        CompanyFactory,
                        )


class TestReviewModelTestCase(APITestCase):
    """
    Tests review model
    """

    def setUp(self):
        self.review = ReviewFactory()

    def test_review_str(self):
        """
        Test that the user can only list own reviews
        """
        eq_(self.review.__str__(), f'{self.review.reviewer} - {self.review.company}')

class TestCompanyModelTestCase(APITestCase):
    """
    Tests review model
    """

    def setUp(self):
        self.company = CompanyFactory()

    def test_review_str(self):
        """
        Test that the user can only list own reviews
        """
        eq_(self.company.__str__(), self.company.name)
