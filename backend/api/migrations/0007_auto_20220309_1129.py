# Generated by Django 3.2.9 on 2022-03-09 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220309_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]