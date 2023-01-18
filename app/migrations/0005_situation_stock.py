# Generated by Django 4.1.4 on 2023-01-18 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_stock_output_stock_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('stocks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stock')),
            ],
        ),
    ]
