from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    """A service that we use: GitHub, Slack, Discourse, etc.

    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ServiceAlias(models.Model):
    """A user's alias for a service: their username

    """
    class Meta:
        verbose_name_plural = "service aliases"
        pass

    service = models.ForeignKey(Service)
    user = models.ForeignKey(User)
    alias = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class ServiceComponent(models.Model):
    """A component of a service: GitHub repo, Slack channel, etc.

    """
    name = models.CharField(max_length=30)
    service = models.ForeignKey(Service)

    def __str__(self):
        return "{} ({})".format(self.name, str(self.service))


class Role(models.Model):
    """A role for a user: web dev, web contributor, game dev, etc.

    """
    name = models.CharField(max_length=30)
    needs = models.ManyToManyField(ServiceComponent, through='Need',
                                   through_fields=('role', 'component'))

    def __str__(self):
        return self.name


class Need(models.Model):
    """A need for a role to use a component

    This is how we associate a particular role (game dev) with a
    component (game repo, discourse access, etc)

    """
    role = models.ForeignKey(Role)
    component = models.ForeignKey(ServiceComponent)

    def __str__(self):
        return "{} need for {}".format(str(self.role), str(self.component))
