# Generated by Django 3.2.9 on 2021-12-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('violation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='existingComSer',
        ),
        migrations.RemoveField(
            model_name='records',
            name='existingViolation',
        ),
        migrations.RemoveField(
            model_name='records',
            name='remainComSerTime',
        ),
        migrations.AlterField(
            model_name='records',
            name='schoolYear',
            field=models.CharField(max_length=50, verbose_name='schoolYear'),
        ),
        migrations.AlterField(
            model_name='records',
            name='studentID',
            field=models.CharField(max_length=50, verbose_name='studentID'),
        ),
        migrations.AlterField(
            model_name='records',
            name='studentNo',
            field=models.CharField(max_length=50, verbose_name='studentNo'),
        ),
    ]