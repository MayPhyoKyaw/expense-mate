# Generated by Django 5.1 on 2024-10-22 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("expenses_mate", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Balances",
            new_name="Balance",
        ),
        migrations.RenameModel(
            old_name="Expenses",
            new_name="Expense",
        ),
        migrations.RenameModel(
            old_name="ExpenseGroups",
            new_name="ExpenseGroup",
        ),
        migrations.RenameModel(
            old_name="GroupUsers",
            new_name="GroupUser",
        ),
        migrations.RenameModel(
            old_name="Users",
            new_name="User",
        ),
    ]