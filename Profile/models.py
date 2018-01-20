from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    contact_no = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=False, null=False)

    # for event organizers
    business_name = models.CharField(max_length=20, blank=False, null=False)
    business_permit = models.ImageField(upload_to='documents/business_permit/', null=True, blank=True)
    business_plate = models.ImageField(upload_to='documents/business_plate/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', null=True, blank=True)
    is_validated = models.IntegerField(max_length=1, default=0, null=False)
    has_paid = models.IntegerField(max_length=1, default=0, null=False)
    description = models.TextField(default='No description is available.', null=False)

    # for clienteles
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)

