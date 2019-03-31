from django.db import models
from django.utils import timezone

STATUS = (
    (1, 'New'),
    (2, 'Assigned to poller'),
    (3, 'Poll done'),
    (4, 'Assigned to certificator'),
    (5, 'Certificate done'),
    (6, 'Certificate verified'),
    (7, 'Ended'),
)

class Certificate(models.Model):
    certificate_code = models.CharField(max_length=7, unique=True)
    client = models.ForeignKey('certificates.Client', on_delete=models.SET_NULL, null=True , blank=False)
    added_to_database = models.DateTimeField(default=timezone.now)
    poller = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name="poller", blank=True)
    assigned_to_poller_date = models.DateTimeField(blank=True, null=True)
    certificator = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to_certificator_date = models.DateTimeField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        verbose_name="Status",
        default=1
    )

    def set_status_greater_then(self, status_number):
        if self.status < status_number:
            self.status = status_number
        self.save()

    def assigne_to_poller(self):
        self.assigned_to_poller_date = timezone.now()
        if self.status < 2:
            self.status = 2
        self.save()

    def assigne_to_certificator(self):
         self.assigned_to_certificator_date = timezone.now()
         if self.status < 4:
             self.status = 4
         self.save()

    def __str__(self):
        return f"{self.certificate_code} {self.client}"


class Client(models.Model):
    first_name = models.CharField(max_length=120, verbose_name="First name")
    surname = models.CharField(max_length=120, verbose_name="Surname")
    description = models.TextField(verbose_name="Description")
    town = models.CharField(max_length=120, verbose_name="Town")
    street = models.CharField(max_length=120, verbose_name="Street")
    house_number = models.PositiveSmallIntegerField(verbose_name="House number")
    apartment_number = models.PositiveSmallIntegerField(verbose_name="Apartment number", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['surname', 'first_name']




