# Generated by Django 4.2.1 on 2023-05-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troncal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(blank=True, max_length=256, null=True)),
                ('auth_srid', models.IntegerField(blank=True, null=True)),
                ('srtext', models.CharField(blank=True, max_length=2048, null=True)),
                ('proj4text', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': True,
            },
        ),
    ]