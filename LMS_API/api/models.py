from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Role(models.Model):
    """
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  """

    ADMIN = 1
    CEO = 2
    CTO = 3
    AREA_MANAGER = 4
    BRANCH_MANAGER = 5
    ACCOUNTANT = 6
    TEACHER = 7
    STUDENT = 8

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CEO, 'CEO'),
        (CTO, 'CTO'),
        (AREA_MANAGER, 'Area Manger'),
        (BRANCH_MANAGER, 'Branch Manager'),
        (ACCOUNTANT, 'Accountant'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student')
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    roles = models.ManyToManyField(Role)
