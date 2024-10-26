from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import User, ExpenseGroup, GroupUser, Expense, Balance


# Create your views here.
class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses_mate/expense_list.html'

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     print("IndexViewを使ってTOP画面を表示します！")
    #     return self.render_to_response(context)
