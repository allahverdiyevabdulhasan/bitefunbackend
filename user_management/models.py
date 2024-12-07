from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    BIOGRAPHY_MAX_LENGTH = 300

    biography = models.CharField(max_length=BIOGRAPHY_MAX_LENGTH, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    class AccountType(models.TextChoices):
        PERSONAL = 'personal', 'Personal'
        BUSINESS = 'business', 'Business'

    account_type = models.CharField(
        max_length=10,
        choices=AccountType.choices,
        default=AccountType.PERSONAL
    )

    is_private = models.BooleanField(default=False)  # Gizli hesap seçeneği

    def __str__(self):
        return self.username
