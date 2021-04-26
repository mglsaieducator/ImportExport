# Generated by Django 3.1.1 on 2020-12-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0003_remove_devicedata_sno'),
    ]

    operations = [
        migrations.CreateModel(
            name='cl_DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('adhaarNo', models.CharField(blank=True, max_length=20)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('village', models.CharField(blank=True, max_length=30)),
                ('mandal', models.CharField(blank=True, max_length=30)),
                ('district', models.CharField(blank=True, max_length=30)),
                ('pincode', models.CharField(blank=True, max_length=10)),
                ('poNo', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=10)),
                ('latitude', models.CharField(blank=True, max_length=10)),
                ('devNo', models.CharField(blank=True, max_length=20)),
                ('dateInst', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='tp_DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('dob', models.DateField()),
                ('adhaarNo', models.CharField(blank=True, max_length=20)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('village', models.CharField(blank=True, max_length=30)),
                ('mandal', models.CharField(blank=True, max_length=30)),
                ('district', models.CharField(blank=True, max_length=30)),
                ('pincode', models.CharField(blank=True, max_length=10)),
                ('poNo', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=10)),
                ('latitude', models.CharField(blank=True, max_length=10)),
                ('devNo', models.CharField(blank=True, max_length=20)),
                ('dateInst', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='DeviceData',
        ),
    ]