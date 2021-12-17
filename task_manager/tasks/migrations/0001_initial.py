# Generated by Django 3.2.9 on 2021-12-16 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statuses', '0001_initial'),
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labeling',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID'
                )),
                ('label', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='labels.label'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True, serialize=False, verbose_name='ID'
                    )),
                ('name', models.CharField(
                    blank=True, max_length=50
                    )),
                ('description', models.TextField(
                    blank=True, null=True
                )),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name='author', to=settings.AUTH_USER_MODEL
                    )),
                ('executor', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='executor', to=settings.AUTH_USER_MODEL
                    )),
                ('labels', models.ManyToManyField(
                    blank=True, related_name='labels',
                    through='tasks.Labeling', to='labels.Label'
                )),
                ('status', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.PROTECT,
                    to='statuses.status')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='labeling',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to='tasks.task'),
        ),
    ]
