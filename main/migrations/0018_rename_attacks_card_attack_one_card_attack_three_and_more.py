# Generated by Django 4.2.3 on 2023-07-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_card_abilities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='attacks',
            new_name='attack_one',
        ),
        migrations.AddField(
            model_name='card',
            name='attack_three',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='attack_two',
            field=models.JSONField(blank=True, null=True),
        ),
    ]