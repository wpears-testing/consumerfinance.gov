# Generated by Django 2.2.16 on 2020-09-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0040_video_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerpage',
            name='share_and_print',
            field=models.BooleanField(default=False, help_text='Include share and print buttons above page content.'),
        ),
    ]