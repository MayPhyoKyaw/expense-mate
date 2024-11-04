from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin # type: ignore
from django.db import models # type: ignore


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "User"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class ExpenseGroup(models.Model):
    class Meta:
        db_table = "ExpenseGroup"
        verbose_name = "支出グループ"
        verbose_name_plural = "支出グループ"

    group_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User, related_name='shared_expense_groups', blank=True)

    def __str__(self):
        return self.title

class Expense(models.Model):
    class Meta:
        db_table = "Expense"
        verbose_name = "費用"
        verbose_name_plural = "費用"

    expense_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # transaction_type = models.CharField(max_length=10, choices=[('add', 'Add'), ('subtract', 'Subtract'),
    #                                                             ('multiply', 'Multiply'), ('divide', 'Divide')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
