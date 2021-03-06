# Generated by Django 3.1.5 on 2021-09-16 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacinacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agendamento.local')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agendamento.paciente')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamento.vacina')),
            ],
        ),
    ]
