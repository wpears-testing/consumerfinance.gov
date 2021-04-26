# Generated by Django 2.2.16 on 2021-03-09 04:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('teachers_digital_platform', '0025_update_notification_default_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPageHandoutDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document', verbose_name='Student file')),
                ('project', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='handout_documents', to='teachers_digital_platform.ActivityPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActivityPageActivityDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document', verbose_name='Teacher guide')),
                ('project', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_documents', to='teachers_digital_platform.ActivityPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]