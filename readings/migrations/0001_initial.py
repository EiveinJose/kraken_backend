# Generated by Django 4.2.20 on 2025-03-18 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpan', models.CharField(max_length=20)),
                ('meter_serial_number', models.CharField(max_length=20)),
                ('reading_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reading_date', models.DateField()),
                ('flow_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='readings.flowfile')),
            ],
        ),
    ]
