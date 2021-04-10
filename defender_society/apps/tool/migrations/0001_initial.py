# Generated by Django 2.2.18 on 2021-02-12 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Website category name')),
                ('order_num', models.IntegerField(default=99, help_text='Serial number can be used to adjust the order, the smaller the higher the front', verbose_name='Serial Number')),
            ],
            options={
                'verbose_name': 'Tool category',
                'verbose_name_plural': 'Tool category',
                'ordering': ['order_num', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ToolLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='site name')),
                ('description', models.CharField(max_length=100, verbose_name='Site Description')),
                ('link', models.URLField(verbose_name='Website Link')),
                ('order_num', models.IntegerField(default=99, help_text='Serial number can be used to adjust the order, the smaller the higher the front', verbose_name='Serial Number')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tool.ToolCategory', verbose_name='Website Category')),
            ],
            options={
                'verbose_name': 'Recommended tool',
                'verbose_name_plural': 'Recommended tool',
                'ordering': ['order_num', 'id'],
            },
        ),
    ]
