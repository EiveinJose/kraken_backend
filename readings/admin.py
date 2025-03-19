from django.contrib import admin
from .models import MeterReading, FlowFile

@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('mpan', 'meter_serial_number', 'reading_value', 'reading_date', 'flow_file')
    search_fields = ('mpan', 'meter_serial_number')

@admin.register(FlowFile)
class FlowFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'uploaded_at')
