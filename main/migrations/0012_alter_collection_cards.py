# Generated by Django 4.2.3 on 2023-07-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_card_abilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='cards',
            field=models.ManyToManyField(blank=True, default=None, related_name='inCollection', to='main.card'),
        ),
    ]
