# Generated by Django 3.1.7 on 2021-03-29 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='last_update',
            new_name='last_updated',
        ),
    ]
