from django.contrib.auth.models import User

# Create your models here.

class Profile(User):
    def __str__(self) -> str:
        return self.email

