# Generated by Django 5.1.5 on 2025-01-24 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_test_dest_host_alter_test_source_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(help_text='Enter a brief description of the location', max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='host',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='tests.location'),
        ),
    ]
