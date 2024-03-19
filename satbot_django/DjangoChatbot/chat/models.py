from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('professor', 'Professor'),
    )
    user_id = models.BigAutoField(primary_key=True)  # Using BigAutoField for future-proofing
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='student')


    def __str__(self):
        return self.username
