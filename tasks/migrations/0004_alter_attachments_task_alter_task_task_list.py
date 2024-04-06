# Generated by Django 5.0.3 on 2024-04-06 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_attachments_task_alter_task_task_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='tasks.task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.tasklist'),
            preserve_default=False,
        ),
    ]
