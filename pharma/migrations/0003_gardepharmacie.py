# Generated by Django 5.1.1 on 2024-09-20 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0002_pharmacie_ville'),
    ]

    operations = [
        migrations.CreateModel(
            name='GardePharmacie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gardes', to='pharma.periode')),
                ('pharmacie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gardes', to='pharma.pharmacie')),
            ],
        ),
    ]
