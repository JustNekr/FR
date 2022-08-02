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
    client_code = PhoneCodeModelSerializer(read_only=False, many=False)
    client_tag = TagModelSerializer(read_only=False, many=False)

    class Meta:
        model = Sending
        fields = ('sending_start', 'sending_end', 'text', 'client_code', 'client_tag')


class MessageModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('sending_date', 'status', 'client_id', 'sending_id')


class ClientModelSerializer(HyperlinkedModelSerializer):
    tag = TagModelSerializer()
    mobile_code = PhoneCodeModelSerializer()

    class Meta:
        model = Client
        fields = ('phone_number', 'mobile_code', 'tag', 'timezone')


