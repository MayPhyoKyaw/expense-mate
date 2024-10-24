# Generated by Django 5.1 on 2024-10-21 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExpenseGroups",
            fields=[
                ("group_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=255)),
                ("password_hash", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="GroupUsers",
            fields=[
                ("group_user_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenses_mate.expensegroups",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenses_mate.users",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expenses",
            fields=[
                ("expense_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_name", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[
                            ("add", "Add"),
                            ("subtract", "Subtract"),
                            ("multiply", "Multiply"),
                            ("divide", "Divide"),
                        ],
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenses_mate.expensegroups",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenses_mate.users",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="expensegroups",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="expenses_mate.users"
            ),
        ),
        migrations.CreateModel(
            name="Balances",
            fields=[
                ("balance_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "balance_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenses_mate.expensegroups",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenses_mate.users",
                    ),
                ),
            ],
        ),
    ]
