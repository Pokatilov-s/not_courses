# Generated by Django 5.0.3 on 2024-05-24 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forge', '0004_alter_course_status'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionsdetails',
            name='course_uuid',
            field=models.ForeignKey(db_column='course_uuid', default=1, on_delete=django.db.models.deletion.PROTECT, to='forge.course'),
            preserve_default=False,
        ),
    ]