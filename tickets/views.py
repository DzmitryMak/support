from django.shortcuts import render
from rest_framework import generics
from .serializers import TicketSerializer, TicketListSerializer
from .models import Ticket


class TicketCreate(generics.CreateAPIView):
    serializer_class = TicketSerializer

class TicketList(generics.ListAPIView):
    serializer_class = TicketListSerializer
    queryset =Ticket.objects.all()

