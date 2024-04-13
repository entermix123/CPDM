from django.contrib.auth import get_user_model
from rest_framework import serializers

from CPDM.accounts.models import Profile

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'user')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'is_staff', 'is_active', 'profile']
        read_only_fields = ['id', 'is_staff', 'is_active']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = super().update(instance, validated_data)

        if profile_data:
            profile, _ = Profile.objects.get_or_create(user=user)
            profile_serializer = ProfileSerializer(profile, data=profile_data, partial=True)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()

        return user


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def to_representation(self, instance):
        # Exclude password field from representation
        ret = super().to_representation(instance)
        ret.pop('password', None)
        return ret


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email']
        read_only_fields = ['id', 'email']

    def validate(self, attrs):
        user = self.context['request'].user
        if user != self.instance:
            raise serializers.ValidationError("You can only delete your own account.")
        return attrs

    def delete(self):
        self.instance.delete()

