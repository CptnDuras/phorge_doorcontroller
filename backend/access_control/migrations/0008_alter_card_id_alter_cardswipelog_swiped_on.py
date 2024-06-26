# Generated by Django 5.0.6 on 2024-06-17 23:38

import datetime
import uuid6
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0007_alter_card_id_alter_card_last_swiped_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.UUIDField(default=uuid6.uuid7, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cardswipelog',
            name='swiped_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 17, 23, 38, 23, 955807, tzinfo=datetime.timezone.utc)),
        ),
    ]
