# Generated by Django 2.0.2 on 2018-02-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0004_secret_game_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='warnings_remaining',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='secret',
            name='guesses_remaining',
            field=models.IntegerField(default=6),
        ),
    ]