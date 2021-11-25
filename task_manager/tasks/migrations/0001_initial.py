# Generated by Django 3.2.9 on 2021-11-25 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statuses', '0002_alter_status_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='author',
                    to=settings.AUTH_USER_MODEL,
                )),
                ('executor', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='executor',
                    to=settings.AUTH_USER_MODEL,
                )),
                ('status', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='statuses.status',
                )),
                ('tags', models.ManyToManyField(
                    blank=True,
                    related_name='tags',
                    to='tasks.Tag',
                )),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'ordering': ['-created'],
            },
        ),
    ]
