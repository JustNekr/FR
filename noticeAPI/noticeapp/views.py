from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from .models import Sending, Message, Client
from .serializers import SendingModelSerializer, MessageModelSerializer, ClientModelSerializer


class SendingModelViewSet(ModelViewSet):
    queryset = Sending.objects.all()
    serializer_class = SendingModelSerializer

    # def create(self, request, *args, **kwargs):
    #     print(request, *args, **kwargs)
    #     sending = Sending.objects.create(
    #         sending_start=request.data['sending_start'],
    #         text=request.data['text'],
    #         sending_end=request.data['sending_end'],
    #     )
    #     sending.save()
    #     return super(SendingModelViewSet, self).create(request, *args, **kwargs)



class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer


class ClientModelViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
