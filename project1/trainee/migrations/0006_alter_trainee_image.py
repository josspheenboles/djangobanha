# Generated by Django 4.1 on 2025-03-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0005_trainee_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='image',
            field=models.ImageField(null=True, upload_to='trainee/imgs'),
        ),
    ]
