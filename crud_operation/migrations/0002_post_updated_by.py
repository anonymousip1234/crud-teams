# Generated by Django 4.0.5 on 2022-07-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
