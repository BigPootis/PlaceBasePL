# Generated by Django 4.2.7 on 2023-11-30 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='files/events'),
            preserve_default=False,
        ),
    ]
