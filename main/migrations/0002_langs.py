# Generated by Django 4.1 on 2022-09-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Langs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('c_code', models.CharField(max_length=10)),
                ('l_code', models.CharField(max_length=10)),
            ],
        ),
    ]
