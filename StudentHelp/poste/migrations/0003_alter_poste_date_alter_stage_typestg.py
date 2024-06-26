# Generated by Django 5.0.2 on 2024-04-21 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0002_alter_poste_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 21, 0, 34, 21, 604017, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='stage',
            name='typeStg',
            field=models.DecimalField(choices=[(1, 'ouvrier'), (2, 'technicien'), (3, 'PFE')], decimal_places=0, default=1, max_digits=1),
        ),
    ]
