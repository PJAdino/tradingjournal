# Generated by Django 4.2.6 on 2023-10-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(max_length=6)),
                ('opening_price', models.FloatField()),
                ('closing_price', models.FloatField()),
                ('take_profit', models.FloatField()),
                ('stop_loss', models.FloatField()),
                ('lot_size', models.FloatField()),
                ('trade_screenshort', models.ImageField(null=True, upload_to='uploads')),
                ('date_added', models.CharField(max_length=10)),
                ('reason', models.TextField(max_length=200)),
                ('result', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
