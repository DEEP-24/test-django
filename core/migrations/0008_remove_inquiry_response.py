# Generated by Django 5.0.7 on 2024-07-15 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_inquiry_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='response',
        ),
    ]