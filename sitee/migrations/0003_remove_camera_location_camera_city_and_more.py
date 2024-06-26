# Generated by Django 4.2.11 on 2024-04-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sitee", "0002_remove_camera_screenshot_camera_data_camera_mime"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="camera",
            name="location",
        ),
        migrations.AddField(
            model_name="camera",
            name="city",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="camera",
            name="country_code",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="camera",
            name="latitude",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="camera",
            name="longitude",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="camera",
            name="region_code",
            field=models.CharField(default="", max_length=100),
        ),
    ]
