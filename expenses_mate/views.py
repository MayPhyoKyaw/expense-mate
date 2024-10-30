from django.db import models # type: ignore
from django.views.generic import ListView # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.db.models import Sum # type: ignore
from .models import User, ExpenseGroup, Expense, Balance
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.contrib.auth import authenticate, login # type: ignore

# User Views
# class UserListView(generic.ListView):
#     model = User
#     template_name = 'user_list.html'  # Specify your template here

# class UserCreateView(generic.CreateView):
#     model = User
#     template_name = 'user_form.html'  # Specify your template here
#     fields = ['name', 'email', 'password_hash']
#     success_url = reverse_lazy('user_list')  # Redirect after creating a user

# class UserDetailView(generic.DetailView):
#     model = User
#     template_name = 'user_detail.html'  # Specify your template here

# class UserUpdateView(generic.UpdateView):
#     model = User
#     template_name = 'user_form.html'  # Specify your template here
#     fields = ['name', 'email', 'password_hash']
#     success_url = reverse_lazy('user_list')

# class UserDeleteView(generic.DeleteView):
#     model = User
#     template_name = 'user_confirm_delete.html'  # Specify your template here
#     success_url = reverse_lazy('user_list')

# ExpenseGroup Views
class ExpenseGroupListView(LoginRequiredMixin, ListView):
    model = ExpenseGroup
    template_name = 'expenses_mate/expense_group_list.html'
    context_object_name = 'expenses_group'
    login_url = 'expenses_mate:account_login'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            total_expense=Sum('expense__amount', output_field=models.DecimalField())
        )
        return queryset

# class ExpenseGroupCreateView(generic.CreateView):
#     model = ExpenseGroup
#     template_name = 'expensegroup_form.html'  # Specify your template here
#     fields = ['title', 'created_by']
#     success_url = reverse_lazy('expense_group_list')

# class ExpenseGroupDetailView(generic.DetailView):
#     model = ExpenseGroup
#     template_name = 'expensegroup_detail.html'  # Specify your template here

# class ExpenseGroupUpdateView(generic.UpdateView):
#     model = ExpenseGroup
#     template_name = 'expensegroup_form.html'  # Specify your template here
#     fields = ['title', 'created_by']
#     success_url = reverse_lazy('expense_group_list')

# class ExpenseGroupDeleteView(generic.DeleteView):
#     model = ExpenseGroup
#     template_name = 'expensegroup_confirm_delete.html'  # Specify your template here
#     success_url = reverse_lazy('expense_group_list')

# Expense Views
class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses_mate/expenses_list.html'
    context_object_name = 'expenses'
    login_url = 'expenses_mate:account_login'

# class ExpenseCreateView(generic.CreateView):
#     model = Expense
#     template_name = 'expense_form.html'  # Specify your template here
#     fields = ['group_id', 'user_id', 'item_name', 'amount', 'transaction_type']
#     success_url = reverse_lazy('expense_list')

# class ExpenseDetailView(generic.DetailView):
#     model = Expense
#     template_name = 'expense_detail.html'  # Specify your template here

# class ExpenseUpdateView(generic.UpdateView):
#     model = Expense
#     template_name = 'expense_form.html'  # Specify your template here
#     fields = ['group_id', 'user_id', 'item_name', 'amount', 'transaction_type']
#     success_url = reverse_lazy('expense_list')

# class ExpenseDeleteView(generic.DeleteView):
#     model = Expense
#     template_name = 'expense_confirm_delete.html'  # Specify your template here
#     success_url = reverse_lazy('expense_list')

# # Balance Views
# class BalanceListView(generic.ListView):
#     model = Balance
#     template_name = 'balance_list.html'  # Specify your template here

# class BalanceCreateView(generic.CreateView):
#     model = Balance
#     template_name = 'balance_form.html'  # Specify your template here
#     fields = ['group_id', 'user_id', 'balance_amount']
#     success_url = reverse_lazy('balance_list')

# class BalanceDetailView(generic.DetailView):
#     model = Balance
#     template_name = 'balance_detail.html'  # Specify your template here

# class BalanceUpdateView(generic.UpdateView):
#     model = Balance
#     template_name = 'balance_form.html'  # Specify your template here
#     fields = ['group_id', 'user_id', 'balance_amount']
#     success_url = reverse_lazy('balance_list')

# class BalanceDeleteView(generic.DeleteView):
#     model = Balance
#     template_name = 'balance_confirm_delete.html'  # Specify your template here
#     success_url = reverse_lazy('balance_list')
