import os
from django.core.management.base import BaseCommand
from readings.models import FlowFile, MeterReading

class Command(BaseCommand):
    help = 'Import a D0010 meter reading file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the D0010 file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        # Check if the file exists
        if not os.path.exists(file_path):
            self.stderr.write(f"File not found: {file_path}")
            return
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Create an entry for this file in the database
        flow_file = FlowFile.objects.create(filename=os.path.basename(file_path))
        
        # Process each line in the file
        for line in lines:
            parts = line.strip().split('|')  # Assuming fields are separated by '|'
            
            if len(parts) < 4:
                continue  # Skip invalid lines
            
            MeterReading.objects.create(
                mpan=parts[0],
                meter_serial_number=parts[1],
                reading_value=float(parts[2]),
                reading_date=parts[3],  # YYYY-MM-DD format
                flow_file=flow_file
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {file_path}'))
