# Generated by Django 5.1.1 on 2024-10-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0007_contadordata_timestamp_umidadedata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contadordata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='luminosidadedata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='temperaturadata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='umidadedata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]