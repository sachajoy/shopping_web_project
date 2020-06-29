from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, password, mob_no, fname, lname):
        if email is None:
            raise ValueError("User must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            fname = fname,
            lname = lname,
            mob_no = mob_no
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, mob_no, fname, lname):
        user = self.create_user(email, password,
                                mob_no, fname, lname)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, default="")
    lname = models.CharField(max_length=255)
    mob_no = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    add = models.TextField(default="")
    city = models.CharField(max_length=75, default="")
    pincode = models.CharField(max_length=10, default="")
    type = models.IntegerField(default=1)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mob_no", "fname", "lname"]

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)

    def get_short_name(self):
        return "{}".format(self.email)

    def get_long_name(self):
        return "{} {}, {}".format(self.fname, self.lname, self.email)