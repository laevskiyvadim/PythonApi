# Generated by Django 4.0.3 on 2022-04-23 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PythonApi', '0006_alter_tasks_stageofexecution'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='Responsible',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='StageOfExecution',
            field=models.CharField(choices=[('Задачи', 'Задачи'), ('В работе', 'Вработе'), ('Тестирование', 'Тестирование'), ('Завершенные', 'Завершенные')], default='Задачи', max_length=20, verbose_name='Стадия'),
        ),
    ]
