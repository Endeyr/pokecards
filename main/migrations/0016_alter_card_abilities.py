# Generated by Django 4.2.3 on 2023-07-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_card_abilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='abilities',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
