# Generated by Django 5.1 on 2024-10-22 14:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('client', models.CharField(max_length=100)),
                ('article_name', models.CharField(max_length=100)),
                ('article_quantity', models.IntegerField()),
                ('ttc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
