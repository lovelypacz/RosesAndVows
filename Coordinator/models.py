from django.db import models


class Coordinator_Data(models.Model):

    user_id = models.ForeignKey('auth.User')
    business_name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=20)


