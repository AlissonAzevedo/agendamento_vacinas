# Generated by Django 3.1.5 on 2021-09-16 01:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0002_vacinacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacinacao',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamento.local'),
        ),
        migrations.AlterField(
            model_name='vacinacao',
            name='vacina',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='agendamento.vacina'),
        ),
    ]
