# Generated by Django 2.1.5 on 2019-02-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20190219_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='platform',
            field=models.CharField(choices=[('WB', 'Web'), ('AP', 'Mobile App'), ('DS', 'DeskTop App'), ('IM', 'Imbedded'), ('ET', 'ETC')], default='ET', max_length=2),
        ),
    ]
