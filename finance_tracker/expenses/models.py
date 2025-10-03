
# Create your models here.
from django.db import models

class Expense(models.Model):
    TRANSACTION_MODES = (
        ('UPI', 'UPI'),
        ('CARD', 'Card'),
        ('CASH', 'Cash'),
    )

    CATEGORY_CHOICES = (
        ('food', 'Food & Dining'),
        ('transport', 'Transportation'),
        ('bills', 'Utilities & Bills'),
        ('entertainment', 'Entertainment'),
        ('shopping', 'Shopping'),
        ('education', 'Education'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    merchant = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    payment_mode = models.CharField(max_length=10, choices=TRANSACTION_MODES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    transaction_type = models.CharField(max_length=10, choices=(('debit','Debit'), ('credit','Credit')))
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.merchant} - {self.amount} on {self.transaction_date}"
