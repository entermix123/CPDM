from django.contrib.auth import get_user_model
from rest_framework import serializers

from CPDM.accounts.serielizers import UserSerializer
from CPDM.activities.models import Activity

UserModel = get_user_model()


class ActivityBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ActivityListSerializer(ActivityBaseSerializer):
    user = UserSerializer(many=False, read_only=True)


class ActivityCreateSerializer(ActivityBaseSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['owner',]

    def create(self, validated_data):
        user = self.context['request'].user
        activity = Activity(**validated_data)
        activity.owner = user
        activity.save()
        return activity


class ActivityUpdateSerializer(ActivityBaseSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['owner',]

    def update(self, instance, validated_data):
        activity = Activity(**validated_data)
        owner = instance.owner
        activity.owner = owner
        activity.save()


class ActivityDetailsSerializer(ActivityBaseSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['owner',]
        lookup_field = 'pk'


class ActivityDeleteSerializer(ActivityBaseSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['owner',]
        lookup_field = 'pk'
