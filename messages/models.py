from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Message(models.Model):

    subject = models.CharField(max_length=70, null=False)
    sent_by = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False)
    phone_number = PhoneNumberField(null=False)
    time = models.DateTimeField(auto_now=True)
    body_text = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return '{} -> {} -> {}'.format(self.sent_by, self.phone_number, self.email)