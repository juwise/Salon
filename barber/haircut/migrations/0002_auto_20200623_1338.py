# Generated by Django 2.1.1 on 2020-06-23 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haircut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='haircut',
        ),
        migrations.RemoveField(
            model_name='haircut',
            name='location',
        ),
        migrations.RemoveField(
            model_name='haircut',
            name='price',
        ),
        migrations.RemoveField(
            model_name='haircut',
            name='type',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
