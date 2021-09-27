from django.db import models

# Create your models here.

class Results(models.Model):
    # The fields in the database are number1, number2 and answer.
    number1 = models.CharField(max_length=512, blank=False, null=False)
    number2 = models.CharField(max_length=512, blank=False, null=False)
    answer = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return f"Number1: {self.number1} + Number2: {self.number2} = {self.answer}"