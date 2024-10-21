from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ExpenseGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GroupUsers(models.Model):
    group_user_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroups, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} in {self.group_id}'

class Expenses(models.Model):
    expense_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroups, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('add', 'Add'), ('subtract', 'Subtract')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

class Balances(models.Model):
    balance_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroups, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id} balance in {self.group_id}'
