# Generated by Django 3.0.5 on 2020-05-09 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20200428_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('notes', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
        migrations.RenameField(
            model_name='amino',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='bcaa',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='beta',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='caffeine',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='lc',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='newone',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='pre',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='protein',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='recovery',
            old_name='Url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='Url',
            new_name='URL',
        ),
        migrations.AlterField(
            model_name='amino',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='amino',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='bcaa',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='bcaa',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='beta',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='beta',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='caffeine',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='caffeine',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='lc',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='lc',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='newone',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='newone',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='pre',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='pre',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='protein',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='protein',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='Flavors',
            field=models.CharField(default='No flavors listed', max_length=25),
        ),
        migrations.AlterField(
            model_name='test',
            name='TopFlavor',
            field=models.CharField(default='No top Flavor', max_length=100),
        ),
    ]
