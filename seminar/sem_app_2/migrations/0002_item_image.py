# Generated by Django 5.0.4 on 2024-05-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem_app_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
