# Generated by Django 4.1 on 2025-03-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
