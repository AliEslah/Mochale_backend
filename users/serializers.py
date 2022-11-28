from rest_framework import serializers
from users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "password",
        )
        read_only_fields = ("full_name", "id")
        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"write_only": True},
            "last_name": {"write_only": True},
        }

    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            user_type=validated_data["user_type"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
