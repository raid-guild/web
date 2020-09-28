# Generated by Django 2.2.4 on 2020-09-14 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0148_add_brightid_status'),
        ('grants', '0079_auto_20200914_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='twitter_verified',
            field=models.BooleanField(default=False, help_text='The owner grant has verified the twitter account'),
        ),
        migrations.AddField(
            model_name='grant',
            name='twitter_verified_at',
            field=models.DateTimeField(blank=True, help_text='At what time and date what verified this grant', null=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='twitter_verified_by',
            field=models.ForeignKey(blank=True, help_text='Team member who verified this grant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Profile'),
        ),
    ]
