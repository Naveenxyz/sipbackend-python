# Generated by Django 2.1.7 on 2019-03-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20190305_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_user',
            name='age_status',
            field=models.CharField(default='below 20', max_length=100),
        ),
    ]