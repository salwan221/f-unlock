# Generated by Django 2.0.9 on 2018-11-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlocker', '0003_auto_20181108_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/onetime/')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
