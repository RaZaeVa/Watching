from django.contrib.auth.base_user import BaseUserManager


from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, username, password=None):
        """
        Создает и сохраняет пользователя с указанным номером телефона, именем пользователя и паролем.
        """

        user = self.model(
            phone_number=phone_number,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Создает и сохраняет суперпользователя с указанным именем пользователя, адресом электронной почты и паролем.
        """
        user = self.model(
            username=username,
            email=email,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user



