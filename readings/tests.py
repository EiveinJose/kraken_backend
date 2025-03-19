from django.test import TestCase
from readings.models import MeterReading, FlowFile

class MeterReadingTestCase(TestCase):
    def setUp(self):
        self.flow_file = FlowFile.objects.create(filename="testfile.txt")
        self.reading = MeterReading.objects.create(
            mpan="123456789",
            meter_serial_number="ABC123",
            reading_value=100.50,
            reading_date="2024-03-13",
            flow_file=self.flow_file
        )

    def test_meter_reading_creation(self):
        self.assertEqual(self.reading.mpan, "123456789")
        self.assertEqual(self.reading.reading_value, 100.50)
