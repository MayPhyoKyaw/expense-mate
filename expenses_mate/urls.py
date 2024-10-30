from django.urls import path # type: ignore
from .views import *
from django.contrib.auth import views as auth_views # type: ignore

app_name = 'expenses_mate'

urlpatterns = [
    # path('', ExpenseListView.as_view(), name="expenses_group_list"),
    path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='account_login'),
    
    # path('users/', UserListView.as_view(), name='user_list'),
    # path('users/create/', UserCreateView.as_view(), name='user_create'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    # path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    
    path('', ExpenseGroupListView.as_view(), name='expense_group_list'),
    # path('expensegroups/create/', ExpenseGroupCreateView.as_view(), name='expensegroup_create'),
    # path('expensegroups/<int:pk>/', ExpenseGroupDetailView.as_view(), name='expensegroup_detail'),
    # path('expensegroups/<int:pk>/update/', ExpenseGroupUpdateView.as_view(), name='expensegroup_update'),
    # path('expensegroups/<int:pk>/delete/', ExpenseGroupDeleteView.as_view(), name='expensegroup_delete'),

    path('expenses/', ExpenseListView.as_view(), name='expenses_list'),
    # path('expenses/create/', ExpenseCreateView.as_view(), name='expense_create'),
    # path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense_detail'),
    # path('expenses/<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense_update'),
    # path('expenses/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),

    # path('balances/', BalanceListView.as_view(), name='balance_list'),
    # path('balances/create/', BalanceCreateView.as_view(), name='balance_create'),
    # path('balances/<int:pk>/', BalanceDetailView.as_view(), name='balance_detail'),
    # path('balances/<int:pk>/update/', BalanceUpdateView.as_view(), name='balance_update'),
    # path('balances/<int:pk>/delete/', BalanceDeleteView.as_view(), name='balance_delete'),

]
