from rest_framework.test import APITestCase, APIClient
from parameterized import parameterized
import json

from .factories import UserFactory
from ..models import User
from django.conf import settings


class UserTests(APITestCase):
    databases = (settings.WRITER_DATABASE, settings.READER_DATABASE, )

    @classmethod
    def setUpClass(cls):
        cls.url = "/api/users/"

        # auth用のdummy user
        cls.dummy_admin = UserFactory(is_active=True,
                                      is_superuser=True)
        return super().setUpClass()

    def get_dummy_admin(self):
        admin = UserFactory(is_active=True,
                            is_superuser=True)
        return admin

    # パラメータ組み合わせで実行
    @parameterized.expand([
        (1, 2),
        (20, 21),
    ])
    def test_ユーザアカウントの数を確認する(self, create_user, expected_user):
        """
        listで取得するユーザの数を検証

        create_user: API実行時に作成しておくユーザ数
        expected_user: API実行時に取得できるはずのユーザ数
        """
        [UserFactory() for _ in range(create_user)]

        # ユーザを作れているか確認
        # dummy分createより1多い
        assert User.objects.count() == expected_user

        # setUpClassでclientを作ると、なぜか認証が通らないためtest内で定義
        client = APIClient()
        client.force_authenticate(user=self.dummy_admin)

        # api実行
        response = client.get(self.url)

        resp_dict = json.loads(response.content)

        # responseの中身を確認
        # 詳細は略。想定した数のデータが取得できているか
        assert resp_dict['count'] == expected_user
        assert len(resp_dict['results']) == expected_user

    def test_アクセストークンなしで実行しエラーになる(self):
        client = APIClient()
        response = client.get(self.url)
        assert response.status_code == 401
