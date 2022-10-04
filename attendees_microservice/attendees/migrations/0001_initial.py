# Generated by Django 4.0.3 on 2022-10-04 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_href', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attendee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='badge', serialize=False, to='attendees.attendee')),
            ],
        ),
        migrations.AddField(
            model_name='attendee',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='attendees.conferencevo'),
        ),
    ]
