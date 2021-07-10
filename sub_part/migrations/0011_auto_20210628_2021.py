# Generated by Django 3.2.4 on 2021-06-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0010_rename_cd_college_clgd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stdregister',
            old_name='LDA',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='stdregister',
            name='ename',
        ),
        migrations.RemoveField(
            model_name='stdregister',
            name='mname',
        ),
        migrations.RemoveField(
            model_name='stdregister',
            name='mothername',
        ),
        migrations.RemoveField(
            model_name='stdregister',
            name='pschool',
        ),
        migrations.RemoveField(
            model_name='stdregister',
            name='school_add',
        ),
        migrations.RemoveField(
            model_name='stdregister',
            name='school_doc',
        ),
        migrations.AddField(
            model_name='stdregister',
            name='dob',
            field=models.DateField(default=None),
        ),
    ]