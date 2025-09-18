from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class UserProfile(models.Model):
    USERNAME_MAX_LENGTH = 30
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2

    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (DO_NOT_SHOW, "Do not show"),
    ]

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=[MinLengthValidator(2)],
    )
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(6)]
    )
    email = models.EmailField(unique=True)

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            RegexValidator(r'^[A-Za-z]+$', 'Only letters are allowed.')
        ]
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            RegexValidator(r'^[A-Za-z]+$', 'Only letters are allowed.')
        ]
    )
    profile_picture = models.URLField(blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default=DO_NOT_SHOW,
    )

    def __str__(self):
        return self.username