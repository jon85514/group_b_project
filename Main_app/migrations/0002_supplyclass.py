# Generated by Django 4.0.4 on 2022-06-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyClass',
            fields=[
                ('supply_class', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('billing_code', models.CharField(max_length=20)),
                ('rates', models.PositiveIntegerField(blank=True)),
                ('active', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1)),
            ],
            options={
                'db_table': 'SupplyCode',
            },
        ),
    ]
