# Generated by Django 4.0.3 on 2022-04-23 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PythonApi', '0008_alter_assistingintheexecution_unique_together_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssistingInTheExecution',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='Responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
