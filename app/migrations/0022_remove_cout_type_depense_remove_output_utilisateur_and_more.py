# Generated by Django 4.1.4 on 2023-02-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_cout'),
    ]

    operations = [
        migrations.AddField(
            model_name='cout',
            name='nombre_depense',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cout',
            name='cout_total_depense',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
