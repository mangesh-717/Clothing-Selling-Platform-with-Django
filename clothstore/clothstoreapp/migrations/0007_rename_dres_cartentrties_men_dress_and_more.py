# Generated by Django 5.0 on 2024-03-16 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothstoreapp', '0006_rename_fruit_cartentrties_dres_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartentrties',
            old_name='dres',
            new_name='Men_dress',
        ),
        migrations.RenameField(
            model_name='cartentrties',
            old_name='shirtandpant',
            new_name='wamens_dress',
        ),
    ]
