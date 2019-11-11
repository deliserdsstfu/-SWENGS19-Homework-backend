from django.db import models


class EventManager(models.Manager):
    pass


class Event(models.Model):

    event_name = models.TextField()
    event_date = models.DateField()
    objects = EventManager()

    class Meta:
        verbose_name_plural = "events"

    def __str__(self):
        return self.event_name