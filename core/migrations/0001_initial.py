# Generated by Django 3.1.6 on 2021-10-23 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.TextField(default='')),
                ('miniature', models.TextField(default='')),
                ('slug', models.TextField(default='')),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('miniature', models.TextField(default='')),
                ('slug', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('positions', models.IntegerField(default=1)),
            ],
        ),
    ]
