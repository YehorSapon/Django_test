from django.db import models
from django.utils import timezone

# Create your models here.


class PublishingHous(models.Model):
    name = models.CharField(
        verbose_name="Publishing Hous's name",
        max_length=50,
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
