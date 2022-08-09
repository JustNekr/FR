import datetime
import zoneinfo

from django.db.models import F, Subquery, OuterRef, Q
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from .models import Sending, Message, Client, Tag, PhoneCode
from .serializers import SendingModelSerializer, MessageModelSerializer, ClientModelSerializer


class SendingModelViewSet(ModelViewSet):
    queryset = Sending.objects.all()
    serializer_class = SendingModelSerializer

    @action(detail=False)
    def active(self, request):
        active_sending = Sending.objects.filter(
            sending_start__lte=datetime.datetime.now(tz=timezone.get_current_timezone()),
            sending_end__gte=datetime.datetime.now(tz=timezone.get_current_timezone()),
            status='A'
        )
        serializer = self.get_serializer(active_sending, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def clients(self, request, pk):
        codes = PhoneCode.objects.filter(sending__pk=pk)
        tags = Tag.objects.filter(sending__pk=pk)
        clients = Client.objects.filter(
            mobile_code__in=codes,
            tag__in=tags,
        )
        serializer = ClientModelSerializer(clients, many=True)
        return Response(serializer.data)


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer


class ClientModelViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
