from rest_framework import viewsets, permissions
from .models import User
from .serializers import (
    UserListSerializer,
    UserRetrieveSerializer
)

from common.permissions import AdminPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ユーザを取得するAPI

    list:
    ユーザのリストを取得する

    承認済みのユーザが実行可能

    retrieve:
    ユーザの詳細を取得する

    詳細データはlistで取得したユーザIDを指定する
    """
    permission_classes = [permissions.IsAuthenticated,
                          AdminPermission]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]

    filterset_fields = ['is_active']
    search_fields = ['email']

    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        methodによってserializerを変える
        """

        if self.action == 'list':
            return UserListSerializer

        return UserRetrieveSerializer
