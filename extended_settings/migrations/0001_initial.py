# Generated by Django 2.2.3 on 2019-07-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtentedSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Configuration name', max_length=1024, verbose_name='Configuration')),
                ('key', models.CharField(max_length=255, verbose_name='Parameter name')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('enabled', models.BooleanField(default=True, verbose_name='Activation')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
                'db_table': 'django_extended_settings',
                'ordering': ('name', 'key'),
            },
        ),
    ]
