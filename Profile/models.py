from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Female', 'F'),
    ('Male', 'M'),
)


# BUDGET_CHOICES = (
#     ('8000 - 10000', '8000 - 10000'),
#     ('10000 - 12000', '10000 - 12000'),
#     ('12000 - 15000', '12000 - 15000'),
#     ('15000 - 18000', '15000 - 18000'),
#     ('18000 - 20000', '18000 - 20000'),
#     ('20000 - 25000', '20000 - 25000'),
#     ('25000 - 30000', '25000 - 30000'),
#     ('30000 - 50000', '30000 - 50000'),
#     ('50000 - 70000', '50000 - 70000'),
# )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    contact_no = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=False, null=False)

    ##for event organizers

    fax_no = models.CharField(max_length=20)
    tel_no = models.CharField(max_length=20)
    business_name = models.CharField(max_length=20, blank=False, null=False)
    cover_photo = models.ImageField(upload_to='cover_photos/', null=True, blank=True)
    # cover_photo = models.ImageField(upload_to='cover_photos/', default='cover_photos/None/no-img.jpg')
    # business_name = models.CharField(max_length=20, blank=True, null=True)

    ##for clienteles
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    # gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
