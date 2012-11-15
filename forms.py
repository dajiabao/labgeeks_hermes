from django import forms
from django.forms import ModelForm
from labgeeks_hermes.models import Notification


class NotificationForm(ModelForm):
    def save(self, *args, **kwargs):
        inst = ModelForm.save(self, *args, **kwargs)
        return inst

    class Meta:
        model = Notification
