# Generated by Django 3.2 on 2021-05-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netconf', '0004_remove_committeemember_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='title',
            field=models.CharField(default='Developer', max_length=250),
        ),
    ]
