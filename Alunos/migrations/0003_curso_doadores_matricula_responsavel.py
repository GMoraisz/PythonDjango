# Generated by Django 5.1.2 on 2024-11-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alunos', '0002_delete_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('periodo', models.CharField(max_length=50)),
                ('dia_aula', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Doadores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=255)),
                ('cpf_cnpj', models.CharField(max_length=18, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id_matricula', models.AutoField(primary_key=True, serialize=False)),
                ('alunos_idalunos', models.IntegerField()),
                ('descricao', models.TextField()),
                ('data_matricula', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
    ]
