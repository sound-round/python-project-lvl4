# Generated by Django 3.2.9 on 2021-12-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_label_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
