# Generated by Django 4.2.11 on 2024-04-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sitee", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="camera",
            name="screenshot",
        ),
        migrations.AddField(
            model_name="camera",
            name="data",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="camera",
            name="mime",
            field=models.CharField(default="", max_length=100),
        ),
    ]