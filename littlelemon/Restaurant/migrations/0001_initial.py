# Generated by Django 5.1.2 on 2024-10-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_guests', models.IntegerField(default=6)),
                ('booking_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking Records',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField(default=5)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu Items',
            },
        ),
    ]
