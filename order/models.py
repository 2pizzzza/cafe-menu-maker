from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import timedelta, datetime


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    start_order = models.TimeField()
    end_order = models.TimeField()
    total_guests = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True)

    TOTAL_TABLES = 35
    SEATS_PER_TABLE = 4

    def clean(self):
        if self.total_guests <= 0:
            raise ValidationError(_("The number of guests must be greater than zero."))

        if self.start_order >= self.end_order:
            raise ValidationError(_("The start time of the reservation must be earlier than the end time."))

        start_datetime = datetime.combine(self.date, self.start_order)
        end_datetime = datetime.combine(self.date, self.end_order)
        max_duration = timedelta(hours=5)

        if end_datetime - start_datetime > max_duration:
            raise ValidationError(_("Tables cannot be reserved for more than 5 hours."))

        required_tables = (self.total_guests + self.SEATS_PER_TABLE - 1) // self.SEATS_PER_TABLE

        overlapping_orders = Order.objects.filter(
            date=self.date,
            start_order__lt=self.end_order,
            end_order__gt=self.start_order
        )

        reserved_tables = sum(
            (order.total_guests + self.SEATS_PER_TABLE - 1) // self.SEATS_PER_TABLE for order in overlapping_orders
        )

        if reserved_tables + required_tables > self.TOTAL_TABLES:
            raise ValidationError(_("There are not enough tables available for the specified time."))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.total_guests} guests on {self.date}"
