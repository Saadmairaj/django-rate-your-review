# Generated by Django 3.1.7 on 2021-11-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_consent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consent',
            name='status',
            field=models.CharField(choices=[('DENY', 'DENY'), ('GRANTED', 'GRANTED'), ('REVOKE', 'REVOKE')], max_length=7),
        ),
    ]
