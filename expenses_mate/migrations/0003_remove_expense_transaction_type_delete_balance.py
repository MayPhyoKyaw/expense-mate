# Generated by Django 5.1 on 2024-11-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("expenses_mate", "0002_delete_groupuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expense",
            name="transaction_type",
        ),
        migrations.DeleteModel(
            name="Balance",
        ),
    ]
