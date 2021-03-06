# Generated by Django 3.2 on 2021-05-01 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('venue', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('venue', models.CharField(max_length=250)),
                ('fromdate', models.CharField(max_length=250)),
                ('todate', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('presenter', models.CharField(choices=[('Attendee', 'Attendee'), ('Presenter', 'Presenter')], default='Attendee', max_length=150)),
                ('topic_to_Present', models.CharField(max_length=250)),
                ('topic_description', models.TextField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netconf.day')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netconf.participant')),
            ],
        ),
    ]
