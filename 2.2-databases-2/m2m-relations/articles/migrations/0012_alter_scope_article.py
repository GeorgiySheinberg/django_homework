# Generated by Django 5.0.4 on 2024-04-12 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_scope_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Заголовок'),
        ),
    ]
