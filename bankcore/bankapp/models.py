import uuid
import datetime
from django.db import models

class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = models.TextField(max_length=255, blank=False, null=False)
    base_url = models.TextField(max_length=255, blank=False, null=False)
    scrapping_period = models.IntegerField(blank=False, null=False)
    status = models.TextField(max_length=50, blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"
 
    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.name, self.base_url, self.scrapping_period, self.status, self.deleted, self.created_at, self.updated_at)