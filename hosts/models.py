from socket import gethostbyaddr

from django.db import models
from django.utils import timezone
import datetime

class Host(models.Model):
    """
    Model which contains information about a single server host.
    """
    ip = models.GenericIPAddressField(null=False)
    name = models.CharField(max_length=191, null=False, blank=True)
    time = models.DateTimeField()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk is None:
            host_data = gethostbyaddr(self.ip)
            if len(host_data):
                self.name = host_data[0]
                self.save()

    def __str__(self):
        return f"{self.ip} ({self.name})"


class OpenPort(models.Model):
    """
    Model which stores which ports are open on Hosts.
    """
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    port = models.SmallIntegerField(null=False)
