from django.db import models
from django.utils import timezone
from datetime import timedelta

class Subscriber(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم العميل")
    last_payment_date = models.DateField(default=timezone.now, verbose_name="آخر تاريخ دفع")
    is_paid = models.BooleanField(default=True, verbose_name="تم الدفع")

    def next_payment_due(self):
        # بعد 30 يوم من آخر دفع
        return self.last_payment_date + timedelta(days=30)

    def __str__(self):
        return self.name
