# Generated by Django 4.0.3 on 2022-04-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PythonApi', '0007_tasks_responsible_alter_tasks_stageofexecution'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assistingintheexecution',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='assistingintheexecution',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='assistingintheexecution',
            name='task',
        ),
        migrations.RemoveField(
            model_name='assistingintheexecution',
            name='user',
        ),
    ]
