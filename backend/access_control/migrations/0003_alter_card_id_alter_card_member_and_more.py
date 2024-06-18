# Generated by Django 5.0.3 on 2024-03-24 23:59

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("access_control", "0002_rename_card_id_cardswipelog_card_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("018e72e7-b1c1-7be0-a1cb-61df3b88e215"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="member",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="access_control.phorgemember",
            ),
        ),
        migrations.AlterField(
            model_name="cardswipelog",
            name="swiped_on",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 24, 23, 59, 30, 754089)
            ),
        ),
    ]
