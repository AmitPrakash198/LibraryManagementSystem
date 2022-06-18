# Generated by Django 4.0.3 on 2022-06-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_userregistration_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='addbookdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(blank=True, max_length=200, null=True)),
                ('authorname', models.CharField(blank=True, max_length=200, null=True)),
                ('bookcatagory', models.CharField(blank=True, max_length=200, null=True)),
                ('bookisbn', models.CharField(blank=True, max_length=200, null=True)),
                ('bookquantity', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'addbookdetails',
            },
        ),
    ]
