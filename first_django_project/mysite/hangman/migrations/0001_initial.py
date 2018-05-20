# Generated by Django 2.0.2 on 2018-05-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_word', models.CharField(max_length=200)),
                ('guesses_remaining', models.IntegerField(default=6)),
                ('warnings_remaining', models.IntegerField(default=3)),
                ('hints_remaining', models.IntegerField(default=2)),
                ('game_status', models.IntegerField(default=0)),
                ('success_state', models.IntegerField(default=0)),
            ],
        ),
    ]
