from django import forms
from . import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        exclude = ['id']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = models.Certificate
        exclude = ['id', "added_to_database", "assigned_to_poller_date", "assigned_to_certificator_date"]