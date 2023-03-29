# Generated by Django 4.1.1 on 2022-09-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0031_alter_accholder_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='reciver',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=211733935, unique=True),
        ),
        migrations.DeleteModel(
            name='Transfers',
        ),
    ]
