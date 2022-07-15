import datetime
import factory.fuzzy
from django.utils.timezone import make_aware

from ..models import User

# Fakerのlocaleをja-JPに変更
factory.Faker.override_default_locale('ja-JP')

# Fakerのproviderは以下参照
# https://faker.readthedocs.io/en/latest/fakerclass.html


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        database = 'reader'

    email = factory.Faker('email')
    is_staff = factory.fuzzy.FuzzyChoice([True, False])
    is_active = factory.fuzzy.FuzzyChoice([True, False])
    date_joined = factory.fuzzy.FuzzyDateTime(
        start_dt=make_aware(datetime.datetime(2008, 1, 1)),
        end_dt=make_aware(datetime.datetime(2010, 1, 1)))
