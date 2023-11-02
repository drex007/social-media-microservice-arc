from django.db import models
from common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
# Create your models here.


class PostModel(TimeStampedUUIDModel):
  title = models.CharField(verbose_name=_("First Name"), max_length=50, blank=False, null=False)
  body = models.CharField(verbose_name=_("Last Name"), max_length=50, blank=False, null=False)
  author_pkid = models.PositiveIntegerField(default=0, blank=False)
  author_email = models.CharField(max_length=120, blank=True, null=True)
  likes = models.PositiveIntegerField(default=0, blank=True)
  
  
  
  def __str__(self) -> str:
    return f"{self.title} || {self.author_email}"