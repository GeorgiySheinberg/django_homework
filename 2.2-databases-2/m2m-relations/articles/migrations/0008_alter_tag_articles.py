# Generated by Django 5.0.4 on 2024-04-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_scope_article_alter_scope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tag', through='articles.Scope', to='articles.article'),
        ),
    ]
