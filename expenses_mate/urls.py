from django.urls import path # type: ignore
from .views import *
from django.contrib.auth import views as auth_views # type: ignore

app_name = 'expenses_mate'

urlpatterns = [
    # path('', ExpenseListView.as_view(), name="expenses_group_list"),
    path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('', ExpenseGroupListCreateView.as_view(), name='expenses_list_create'),
    path('expenses/<int:group_id>/', ExpenseManageView.as_view(), name='expense_detail'),
    path('share_expense_group/<int:group_id>/', ShareExpenseGroupView.as_view(), name='share_expense_group'),
]
