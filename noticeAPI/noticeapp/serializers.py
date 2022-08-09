import datetime
import zoneinfo

from django.utils import timezone
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Sending, Message, Client, Tag, PhoneCode, Timezone


class TagModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id',)


class PhoneCodeModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PhoneCode
        fields = ('id',)


class SendingModelSerializer(HyperlinkedModelSerializer):
    client_tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    client_code = serializers.PrimaryKeyRelatedField(queryset=PhoneCode.objects.all(), many=True)
    # current_time_test = ReadOnlyField(default=f'{datetime.datetime.now(tz=timezone.utc) > Sending.objects.get(id=1).sending_start} '
    #                                           f'{datetime.datetime.now(tz=timezone.utc)}'
    #                                           f'{Sending.objects.get(id=1).sending_start}')

    class Meta:
        model = Sending
        fields = ('id', 'sending_start', 'sending_end', 'text', 'client_code', 'client_tag')

    def create(self, validated_data):
        instance = super(SendingModelSerializer, self).create(validated_data)

        client_list = Client.objects.filter(mobile_code__in=self.data['client_code'], tag__in=self.data['client_tag'])

        for client in client_list:
            print()

            message = Message(
                client_id=client,
                sending_id=Sending(pk=instance.pk),
            )
            message.save()
        return instance


class MessageModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sending_date', 'status', 'client_id', 'sending_id')


class ClientModelSerializer(HyperlinkedModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=False)
    mobile_code = serializers.PrimaryKeyRelatedField(queryset=PhoneCode.objects.all(), many=False)
    tz = serializers.PrimaryKeyRelatedField(queryset=Timezone.objects.all(), many=False)

    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'mobile_code', 'tag', 'tz')


