# Generated by Django 5.0.2 on 2024-04-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
