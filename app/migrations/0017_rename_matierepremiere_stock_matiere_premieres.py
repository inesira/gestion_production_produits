# Generated by Django 4.1.4 on 2023-02-06 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_matiere_premiere_stock_matierepremiere'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='matierePremiere',
            new_name='matiere_premieres',
        ),
    ]
