from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AuditInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    edited_on = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_by = models.ForeignKey(
        User,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    edited_by = models.ForeignKey(
        User,
        related_name="%(class)s_edited",
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    class Meta:
        abstract = True

class Todo(AuditInfo):
    deadline = models.DateTimeField(default=None, null=True, blank=True)
    title = models.CharField(null=False, blank=False, max_length=100)
    details = models.TextField(null=True, blank=True)
    