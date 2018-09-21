# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class NoticePost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

# Create your models here.
