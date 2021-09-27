# Generated by Django 3.1.5 on 2021-09-16 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCidade', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeEnfermeiro', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('sobrenome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('comorbidade', models.CharField(choices=[('N', 'Nenhum'), ('DM', 'Diabetes mellitus'), ('PCG', 'Pneumopatias cronicas graves'), ('HAR', 'Hipertensao Arterial Resistente (HAR)'), ('DNC', 'Doença neurologicas cronicas'), ('DRC', 'Doença renal cronica')], default='N', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('nomeLocal', models.CharField(max_length=90)),
                ('endereco', models.CharField(max_length=70)),
                ('cidade', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='agendamento.cidade')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ManyToManyField(to='agendamento.Estado'),
        ),
    ]
