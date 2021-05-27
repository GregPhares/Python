# Generated by Django 3.0.5 on 2020-04-29 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amino',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='amino',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='bcaa',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='bcaa',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='beta',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='beta',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='caffeine',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='caffeine',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='lc',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='lc',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='newone',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='newone',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='pre',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='pre',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='protein',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='protein',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='test',
            name='Flavors',
            field=models.CharField(default='No flavor listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='test',
            name='Url',
            field=models.CharField(max_length=1000),
        ),
    ]
