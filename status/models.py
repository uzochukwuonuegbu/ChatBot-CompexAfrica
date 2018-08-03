from django.db import models
from django.conf import settings


class StatusQuerySet(models.QuerySet):
    def get_query_set(self):
        pass

class StatusManager(models.Manager):
    def get_query_set(self):
        return StatusQuerySet(self.model, using=self.db)


class Status(models.Model):
    user   =   models.ForeignKey(settings.AUTH_USER_MODEL)
    content =  models.TextField(null=True, blank=True)

    objects = StatusManager()

    def __str__(self):
        return self.content

