import clearbit

from pyhunter import PyHunter
from django.contrib.auth.models import BaseUserManager

from StarNaviTest.settings import CLEAR_BIT_API_KEY, EMAIL_HUNTER_API_KEY


class UserManager(BaseUserManager):
    use_in_migrations = True
    clearbit.key = CLEAR_BIT_API_KEY
    hunter = PyHunter(EMAIL_HUNTER_API_KEY)

    def create_user(self, email, password, **extra_fields):
        if not self.hunter.email_verifier(email).get('smtp_check'):
            raise ValueError('Email does not exist')
        person = clearbit.Person.find(email=email, stream=True)
        if person is not None:
            extra_fields.setdefault('github_id', person['github']['id'])
            extra_fields.setdefault('github_name', person['github']['handle'])

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
