# Generated by Django 3.2.14 on 2022-07-18 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0214_convert_email_signups_blocks_in_streamfields_to_snippets'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
