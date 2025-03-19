from django.db import models

class FlowFile(models.Model):
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MeterReading(models.Model):
    mpan = models.CharField(max_length=20)
    meter_serial_number = models.CharField(max_length=20)
    reading_value = models.DecimalField(max_digits=10, decimal_places=2)
    reading_date = models.DateField()
    flow_file = models.ForeignKey(FlowFile, on_delete=models.CASCADE, related_name="readings")

    def __str__(self):
        return f"{self.mpan} - {self.reading_value} ({self.reading_date})"
