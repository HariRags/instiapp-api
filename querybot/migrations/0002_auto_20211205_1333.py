# Generated by Django 3.2.9 on 2021-12-05 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('querybot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='query',
            options={'verbose_name': 'Query', 'verbose_name_plural': 'Queries'},
        ),
        migrations.AlterModelOptions(
            name='unresolvedquery',
            options={'verbose_name': 'UnresolvedQuery', 'verbose_name_plural': 'UnresolvedQueries'},
        ),
    ]
