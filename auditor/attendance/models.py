from django.contrib.auth.models import User
from django.db import models


class Meeting(models.Model):
    """A meeting
    """
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    present = models.ManyToManyField(User, through='Attendance',
                                     through_fields=('meeting', 'user'))

    @property
    def head_count(self):
        return self.present.count()

    def __str__(self):
        return self.name


class Attendance(models.Model):
    """A user's meeting attendance
    """
    class Meta:
        unique_together = (
            ('user', 'meeting'),
        )

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    meeting = models.ForeignKey(Meeting)

    def __str__(self):
        return "{} ({})".format(self.user, self.meeting)
