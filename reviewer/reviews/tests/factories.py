import factory
from ..models import (Review,
                      Company,
                      )

from faker import Faker
from reviewer.users.test.factories import UserFactory

fake = Faker()


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = fake.company()


class ReviewFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Review

    summary = fake.text()
    title = fake.bs()
    ip_address = fake.ipv4(network=False, address_class=None, private=None)
    company = CompanyFactory()
    reviewer = UserFactory()
