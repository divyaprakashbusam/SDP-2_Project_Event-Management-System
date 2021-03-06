# Generated by Django 3.2.1 on 2021-05-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book_ground',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Events_list',
            fields=[
                ('eventid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
