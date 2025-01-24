from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field
import uuid


class Location(models.Model):
    """Model representing a perfsonar location."""
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the location')
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this location."""
        return reverse('location-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name


# Create your models here.
class Host(models.Model):
    """Model representing a perfsonar Host."""
    host_name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Please enter a valid DNS Hostname or IP address"
    )

    # location = models.CharField(
    #     max_length=200,
    #     unique=False,
    #     help_text="Please enter the location of the server (PASC, KAD, SDC, etc...)"
    # )

    location = models.ForeignKey('Location', on_delete=models.RESTRICT, null=True)
    
    description = models.CharField(
        max_length=200,
        unique=False,
        help_text="Please enter a brief descriotion of the server"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.host_name

    def get_absolute_url(self):
        """Returns the url to access a particular host instance."""
        return reverse('host-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('host_name'),
                name='host_name_case_insensitive_unique',
                violation_error_message = "Host already exists (case insensitive match)"
            ),
        ]


class Test(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular test instance.")

    """Model representing a test."""
    test_name = models.CharField(
        max_length=200,
        unique=False,
        help_text="Please enter a brief descriotion of the test"
    )

    test_types = (
        ('t', 'throughput'),
        ('l1', 'latency (one-way)'),
        ('rtt', 'latency (round-trip)'),
        ('tr', 'traceroute')
    )
    type = models.CharField(
        max_length=3,
        choices=test_types,
        blank=True,
        default='t',
        help_text='Test Type',
    )

    test_description = models.CharField(max_length=200)

    duration = models.IntegerField()

    source_host = models.ForeignKey('Host', related_name="source_host", on_delete=models.RESTRICT, null=True)
    dest_host = models.ForeignKey('Host', related_name="dest_host", on_delete=models.RESTRICT, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.test_name

    def get_absolute_url(self):
        """Returns the url to access a particular host instance."""
        return f'{self.id} ({self.self.test_name})'

    