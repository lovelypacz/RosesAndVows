from django.db import models
from django.utils import timezone

# Create your models here.

CATEGORY = (
    ('Wedding', 'Wedding'),
    ('Debut', 'Debut'),
    ('Birthday', 'Birthday'),
    ('Thanksgiving', 'Thanksgiving'),
)

class Post(models.Model):

    author = models.ForeignKey('auth.User')
    package_name = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(max_length=20, choices=CATEGORY)
    image = models.ImageField(upload_to = 'package_images/', null=True, blank=True,)
    max_budget = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.package_name
        # return self.title



