from django.contrib import admin
from .models import User, ExpenseGroup, Expense, GroupUser, Balance


# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'password_hash')


class ExpenseGroupsAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'title', 'created_by', 'created_at')


class GroupUsersAdmin(admin.ModelAdmin):
    list_display = ('group_user_id', 'group_id', 'user_id')


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'group_id', 'user_id', 'item_name', 'amount', 'transaction_type')


class BalancesAdmin(admin.ModelAdmin):
    list_display = ('balance_id', 'group_id', 'user_id', 'balance_amount', 'last_updated')


admin.site.register(User, UsersAdmin)
admin.site.register(ExpenseGroup, ExpenseGroupsAdmin)
admin.site.register(GroupUser, GroupUsersAdmin)
admin.site.register(Expense, ExpensesAdmin)
admin.site.register(Balance, BalancesAdmin)
