# Generated by Django 4.2.7 on 2023-12-02 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrdemServico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='admin',
            table='admin',
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='cliente',
        ),
        migrations.AlterModelTable(
            name='equipe',
            table='equipe',
        ),
        migrations.AlterModelTable(
            name='mecanico',
            table='mecanico',
        ),
        migrations.AlterModelTable(
            name='ordemservico',
            table='ordem_servico',
        ),
        migrations.AlterModelTable(
            name='pecas',
            table='pecas',
        ),
        migrations.AlterModelTable(
            name='pecasordemservico',
            table='pecas_ordem_servico',
        ),
        migrations.AlterModelTable(
            name='veiculo',
            table='veiculo',
        ),
    ]