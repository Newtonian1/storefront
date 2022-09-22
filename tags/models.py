from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # ContentType establishes a generic relationship so that the tags app is not dependent on the store app
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # An item type and an ID are required to specify an object in a database (item type -> table, ID -> primary key)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
