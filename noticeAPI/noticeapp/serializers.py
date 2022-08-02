from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Sending, Message, Client


class SendingModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Sending
        fields = ('sending_start', 'sending_end', 'text', 'client_code', 'client_tag')


class MessageModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('sending_date', 'status', 'client_id', 'sending_id')


class ClientModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('phone_number', 'mobile_code', 'tag', 'timezone')

