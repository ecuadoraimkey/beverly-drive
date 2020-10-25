from rest_framework import serializers
from contactrequest.models import ContactRequest

class ContactRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactRequest
        fields = '__all__'