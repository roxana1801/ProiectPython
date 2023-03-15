from django.db import models

SUBSCRIPTION_TYPES = [('individual', 'individual'), ('family', 'family'), ('premium', 'premium')]
SHOW_TYPE = [('movie', 'movie'), ('tv_series', 'tv_series')]

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subscription_type = models.CharField(max_length=10, choices=SUBSCRIPTION_TYPES, default='individual')  # individual/family/premium
    is_logged = models.BooleanField(default=False)


    def __str__(self):
        return f"User(username={self.username}, email={self.email}, is_logged={self.is_logged}, subscription_type={self.subscription_type})"

    def __repr__(self):
        return self.__str__()

class Show(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=SHOW_TYPE)
    subtitle_languages = models.CharField(max_length=200)  # 'ro,eng'
    length_minutes = models.IntegerField()
    nr_of_episodes = models.IntegerField(null=True, blank=True)
    poster = models.CharField(max_length=1000, null=True, blank=True, default=None)

    def __str__(self):
        return f"Show(title={self.title}, type={self.type}, subtitle_languages={self.subtitle_languages}, length_minutes={self.length_minutes}, length_minutes={self.length_minutes})"

    def __repr__(self):
        return self.__str__()


class Provider(models.Model):
    name = models.CharField(max_length=200)
    subscription_price =  models.IntegerField()

    def __str__(self):
        return f"Provider(name={self.name}, subscription_price={self.subscription_price})"

    def __repr__(self):
        return self.__str__()
