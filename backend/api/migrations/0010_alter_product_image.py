# Generated by Django 3.2.9 on 2022-03-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220309_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
