# Generated by Django 3.2.4 on 2021-06-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0003_rename_stdsign_stdsignin'),
    ]

    operations = [
        migrations.CreateModel(
            name='clgsignin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=100)),
                ('re_pass', models.CharField(max_length=100)),
            ],
        ),
    ]
