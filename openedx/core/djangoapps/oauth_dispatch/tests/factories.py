# pylint: disable=missing-docstring

from datetime import datetime, timedelta

import factory
import pytz
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from oauth2_provider.models import AccessToken, RefreshToken, Application

from student.tests.factories import UserFactory


class ApplicationFactory(DjangoModelFactory):
    class Meta(object):
        model = Application

    user = factory.SubFactory(UserFactory)
    client_type = Application.CLIENT_CONFIDENTIAL
    authorization_grant_type = Application.GRANT_AUTHORIZATION_CODE


class AccessTokenFactory(DjangoModelFactory):
    class Meta(object):
        model = AccessToken
        django_get_or_create = ('user', 'application')

    token = FuzzyText(length=32)
    expires = datetime.now(pytz.UTC) + timedelta(days=1)


class RefreshTokenFactory(DjangoModelFactory):
    class Meta(object):
        model = RefreshToken
        django_get_or_create = ('user', 'application')

    token = FuzzyText(length=32)
