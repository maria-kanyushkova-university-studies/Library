# Generated by Django 3.1.3 on 2020-11-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20201111_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),
        migrations.AlterField(
            model_name='book',
            name='rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='code',
            name='is_deleted',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='is_actual',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='is_actual',
            field=models.BooleanField(),
        ),
    ]