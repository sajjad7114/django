from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.decorators import login_required

# Create your models here.

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class User(models.Model):
    username = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=USERNAME_REGEX,
                message='Username must be Alpahnumeric or contain any of the following: ". @ + -" ',
                code='invalid_username'
            )],
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password = models.CharField(max_length=120,null=True, blank=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    owner = models.ForeignKey(User)
    date = models.DateField()
    fromm = models.TimeField()
    untill = models.TimeField()
    title = models.CharField(max_length=255, unique=True)
    note = models.TextField(max_length=255, null=True, blank=True)



