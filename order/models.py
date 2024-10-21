from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import timedelta, datetime, time


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

    WORKING_HOURS_WEEKDAY = (time(11, 0), time(22, 0))
    WORKING_HOURS_WEEKEND = (time(11, 0), time(23, 0))

    @staticmethod
    def get_working_hours(date):
        if date.weekday() < 5:
            return Order.WORKING_HOURS_WEEKDAY
        else:
            return Order.WORKING_HOURS_WEEKEND

    @staticmethod
    def get_free_tables_on_date(date):
        working_hours = Order.get_working_hours(date)
        start_time = datetime.combine(date, working_hours[0])
        end_time = datetime.combine(date, working_hours[1])
        time_slots = []

        current_time = start_time
        while current_time < end_time:
            next_time = current_time + timedelta(hours=1)
            overlapping_orders = Order.objects.filter(
                date=date,
                start_order__lt=next_time.time(),
                end_order__gt=current_time.time()
            )

            reserved_tables = sum(
                (order.total_guests + Order.SEATS_PER_TABLE - 1) // Order.SEATS_PER_TABLE for order in
                overlapping_orders
            )

            free_tables = Order.TOTAL_TABLES - reserved_tables
            time_slots.append({
                'start_time': current_time.time(),
                'end_time': next_time.time(),
                'free_tables': free_tables
            })

            current_time = next_time

        return time_slots

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
