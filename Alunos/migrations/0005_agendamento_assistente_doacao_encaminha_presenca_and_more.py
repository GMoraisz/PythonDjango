# Generated by Django 5.1.2 on 2024-11-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alunos', '0004_aluno_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Assistente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('endereco', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Encaminha',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('data_presenca', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]