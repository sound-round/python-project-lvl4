# Generated by Django 3.2.9 on 2021-12-20 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0002_auto_20211220_1053'),
        ('statuses', '0002_alter_status_name'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labeling',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='tasks.task'
                ),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='author', to=settings.AUTH_USER_MODEL,
                verbose_name='Автор'
                ),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(
                blank=True, null=True, verbose_name='Описание'
                ),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='executor', to=settings.AUTH_USER_MODEL,
                verbose_name='Исполнитель'
                ),
        ),
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(
                blank=True, related_name='labels',
                through='tasks.Labeling', to='labels.Label',
                verbose_name='Метка'
                ),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(
                blank=True, max_length=50, verbose_name='Имя'
                ),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT,
                to='statuses.status', verbose_name='Статус'
                ),
        ),
    ]
