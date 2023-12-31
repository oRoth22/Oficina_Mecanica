# Generated by Django 4.2.7 on 2023-12-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdemServico', '0004_remove_equipe_ordem_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='mecanico',
            field=models.ManyToManyField(to='OrdemServico.Mecanico'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='mecanicos',
            field=models.ManyToManyField(to='OrdemServico.mecanico'),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
