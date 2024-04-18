# Generated by Django 5.0.4 on 2024-04-18 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField()),
                ('respondida_em', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.aluno')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.pergunta')),
            ],
        ),
        migrations.AddConstraint(
            model_name='resposta',
            constraint=models.UniqueConstraint(fields=('aluno', 'pergunta'), name='resposta_unica'),
        ),
    ]
