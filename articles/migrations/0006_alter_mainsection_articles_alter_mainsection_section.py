# Generated by Django 4.1 on 2022-09-05 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_mainsection_options_alter_section_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsection',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='mainsection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.section'),
        ),
    ]
