# Generated by Django 3.2.14 on 2022-08-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0021_communitypost_reported_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communitypost",
            name="anonymous",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]