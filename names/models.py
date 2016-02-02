from __future__ import unicode_literals

from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=254, verbose_name='Name')
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
