# Generated by Django 2.2.6 on 2019-10-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='em_estoque',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
