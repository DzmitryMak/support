from django.urls import path
from .views import TicketCreate, TicketList


urlpatterns = [
    path('create/', TicketCreate.as_view()),
    path('list/', TicketList.as_view()),
]
