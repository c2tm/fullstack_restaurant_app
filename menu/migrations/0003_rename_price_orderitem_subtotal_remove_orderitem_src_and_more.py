# Generated by Django 4.0.2 on 2022-02-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='subtotal',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='src',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='items',
            field=models.JSONField(null=True),
        ),
    ]