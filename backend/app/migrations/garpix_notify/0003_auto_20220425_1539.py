# Generated by Django 3.1 on 2022-04-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_notify', '0002_auto_20220425_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='event',
            field=models.IntegerField(blank=True, choices=[(1, 'Новая бронь')], null=True, verbose_name='Событие'),
        ),
        migrations.AlterField(
            model_name='notifytemplate',
            name='event',
            field=models.IntegerField(blank=True, choices=[(1, 'Новая бронь')], null=True, verbose_name='Событие'),
        ),
    ]
