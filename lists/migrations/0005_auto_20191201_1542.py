# Generated by Django 2.2.3 on 2019-12-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete='CASCADE', to='lists.List'),
        ),
    ]
