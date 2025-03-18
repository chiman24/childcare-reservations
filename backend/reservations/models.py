from django.db import models

# Create your models here.
class Reservation(models.Model):
    parent_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    rehearsal_date = models.DateField()
    num_children = models.PositiveIntegerField()
    
    # Store child ages as a JSON array
    child_ages = models.JSONField()

    special_notes = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto record submission time

    def __str__(self):
        return f"{self.parent_name} - {self.rehearsal_date}"