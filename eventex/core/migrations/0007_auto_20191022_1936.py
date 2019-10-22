# Generated by Django 2.2.5 on 2019-10-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='course',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='inicio'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, verbose_name='titulo'),
        ),
    ]