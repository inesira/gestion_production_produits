# Generated by Django 4.1.4 on 2023-01-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_cout_total_production_cout_production_cout_total_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('tel', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('adress', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45, null=True)),
                ('password', models.CharField(max_length=45, null=True)),
            ],
        ),
    ]
