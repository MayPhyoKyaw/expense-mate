from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ExpenseGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GroupUser(models.Model):
    group_user_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} in {self.group_id}'


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('add', 'Add'), ('subtract', 'Subtract'),
                                                                ('multiply', 'Multiply'), ('divide', 'Divide')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class Balance(models.Model):
    balance_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id} balance in {self.group_id}'
