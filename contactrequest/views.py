from django.shortcuts import render
from rest_framework import viewsets, permissions
from contactrequest.models import ContactRequest
from contactrequest.serializers import ContactRequestSerializer


class ContactRequestViewSet(viewsets.ModelViewSet):
    
    # Browsable API end point for Contact Requests.
    
    queryset = ContactRequest.objects.all().order_by('-time')
    serializer_class = ContactRequestSerializer
