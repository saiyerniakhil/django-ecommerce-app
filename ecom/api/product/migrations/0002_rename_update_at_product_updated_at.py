# Generated by Django 4.2.4 on 2023-08-07 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
