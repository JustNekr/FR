from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Sending, Message, Client, Tag, PhoneCode


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

    class Meta:
        model = Sending
        fields = ('id', 'sending_start', 'sending_end', 'text', 'client_code', 'client_tag')


class MessageModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sending_date', 'status', 'client_id', 'sending_id')


class ClientModelSerializer(HyperlinkedModelSerializer):
    tag = TagModelSerializer()
    mobile_code = PhoneCodeModelSerializer()

    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'mobile_code', 'tag', 'timezone')


