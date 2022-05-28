from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ticket
        fields = ('title', 'content', 'author')


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
