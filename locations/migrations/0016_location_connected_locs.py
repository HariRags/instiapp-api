# Generated by Django 3.2.16 on 2023-08-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0015_auto_20230111_1809"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="connected_locs",
            field=models.TextField(blank=True, null=True),
        ),
    ]