from django.conf import settings
from django.db import models
import string
import random


class URL(models.Model):
    original_url = models.URLField()
    tiny_url = models.CharField(primary_key=True, max_length=5)

    def generate_url(self):
        self.tiny_url = self.reduce_url()
    
    def reduce_url(self):
        alphanumeric = string.ascii_lowercase + string.digits
        return ''.join(random.sample(alphanumeric, 5))

    def __str__(self):
        return "Original URL: {} \nTiny URL: {}".format(self.original_url, self.tiny_url)