from rest_framework import serializers

from .models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'is_staff',
            'is_active'
        )


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        # 除外するフィールド
        exclude = (
            'groups',
            'user_permissions'
        )
