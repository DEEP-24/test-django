# Generated by Django 5.0.7 on 2024-07-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_inquiry_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='property_purchaser',
        ),
        migrations.AddField(
            model_name='inquiry',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
