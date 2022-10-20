# Generated by Django 4.1.2 on 2022-10-15 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='bike_id',
            new_name='bike',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='orders',
            name='rent_day_end',
            field=models.DateTimeField(verbose_name='Ngày trả'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='rent_day_start',
            field=models.DateTimeField(verbose_name='Ngày thuê'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='type_rent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.renttype', verbose_name='Loại thuê'),
        ),
    ]