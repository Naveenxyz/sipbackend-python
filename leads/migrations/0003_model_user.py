# Generated by Django 2.1.7 on 2019-03-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_lead_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_user',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('profile_name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('hash_id', models.CharField(max_length=100)),
            ],
        ),
    ]
