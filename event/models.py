from django.db import models


class Event(models.Model):
    """Events Model"""

    title = models.CharField("Title", max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class ImageForEvent(models.Model):
    """Image Model"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField("Image", upload_to="images/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.event.title
