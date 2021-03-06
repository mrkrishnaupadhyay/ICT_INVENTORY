# Generated by Django 2.0.7 on 2018-08-17 03:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20180817_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='date_of_purchase',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='date_of_purchase',
        ),
        migrations.RemoveField(
            model_name='networkswitch',
            name='date_of_purchase',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='date_of_purchase',
        ),
        migrations.AddField(
            model_name='computer',
            name='date_of_acquire',
            field=models.DateField(default=datetime.date.today, help_text='Enter the date of acquire'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='date_of_acquire',
            field=models.DateField(default=datetime.date.today, help_text='Enter the date of acquire'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='room',
            field=models.ForeignKey(help_text='Select room where it is kept', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Room'),
        ),
        migrations.AddField(
            model_name='networkswitch',
            name='date_of_acquire',
            field=models.DateField(default=datetime.date.today, help_text='Enter the date of acquire'),
        ),
        migrations.AddField(
            model_name='printer',
            name='date_of_acquire',
            field=models.DateField(default=datetime.date.today, help_text='Enter the date of acquire'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='cost',
            field=models.DecimalField(decimal_places=2, help_text='Enter the cost of the item', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='id',
            field=models.CharField(help_text='Enter the ID of the item', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='computer',
            name='model',
            field=models.CharField(default='Generic', help_text='Enter the model of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='computer',
            name='name',
            field=models.CharField(default='Generic', help_text='Enter the brand name of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='cost',
            field=models.DecimalField(decimal_places=2, help_text='Enter the cost of the item', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='id',
            field=models.CharField(help_text='Enter the ID of the item', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='model',
            field=models.CharField(default='Generic', help_text='Enter the model of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(default='Generic', help_text='Enter the brand name of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='networkswitch',
            name='cost',
            field=models.DecimalField(decimal_places=2, help_text='Enter the cost of the item', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='networkswitch',
            name='id',
            field=models.CharField(help_text='Enter the ID of the item', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='networkswitch',
            name='model',
            field=models.CharField(default='Generic', help_text='Enter the model of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='networkswitch',
            name='name',
            field=models.CharField(default='Generic', help_text='Enter the brand name of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='printer',
            name='cost',
            field=models.DecimalField(decimal_places=2, help_text='Enter the cost of the item', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='id',
            field=models.CharField(help_text='Enter the ID of the item', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='printer',
            name='model',
            field=models.CharField(default='Generic', help_text='Enter the model of the item', max_length=50),
        ),
        migrations.AlterField(
            model_name='printer',
            name='name',
            field=models.CharField(default='Generic', help_text='Enter the brand name of the item', max_length=50),
        ),
    ]
