# Generated by Django 4.1 on 2025-03-11 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_alter_track_name'),
        ('trainee', '0004_remove_trainee_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='track',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='track.track'),
            preserve_default=False,
        ),
    ]
