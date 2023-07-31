# Generated by Django 4.2.3 on 2023-07-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_card_tcgplayer_prices_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='cardmarket_prices',
        ),
        migrations.AddField(
            model_name='card',
            name='cardmarket_prices_holo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='cardmarket_prices_normal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='tcgplayer_prices_holo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='tcgplayer_prices_normal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
