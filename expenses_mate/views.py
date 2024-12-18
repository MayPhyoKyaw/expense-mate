from django.db import models # type: ignore
from django.views.generic import View, ListView, FormView, UpdateView# type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.db.models import Sum # type: ignore
from .models import User, ExpenseGroup, Expense
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from .forms import ExpenseGroupForm, ExpenseForm # type: ignore
from django.db.models import Q # type: ignore
from django.shortcuts import get_object_or_404 # type: ignore

class ExpenseGroupListCreateView(LoginRequiredMixin, View):
    template_name = 'expenses_mate/expenses_list.html'
    
    def get(self, request, *args, **kwargs):
        expense_groups = ExpenseGroup.objects.filter(
            Q(created_by=request.user) | Q(shared_with=request.user)
        ).select_related('created_by').annotate(
            total_expense=Sum('expense__amount', output_field=models.DecimalField())
        )
        all_users = User.objects.all()
        form = ExpenseGroupForm()
        context = {
            'expenses_group': expense_groups,
            'form': form,
            'all_users': all_users
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'delete_id' in request.POST:
            # Handle deletion of an expense group
            expense_group = get_object_or_404(ExpenseGroup, group_id=request.POST['delete_id'], created_by=request.user)
            expense_group.delete()
            return redirect('expenses_mate:expenses_list_create')  # Redirect after deletion
        
        form = ExpenseGroupForm(request.POST)
        if form.is_valid():
            expense_group = form.save(commit=False)
            expense_group.created_by = request.user
            expense_group.save()
            form.save_m2m() 
            return redirect('expenses_mate:expenses_list_create') 
        
        expense_groups = ExpenseGroup.objects.filter(
            Q(created_by=request.user) | Q(shared_with=request.user)
        ).select_related('created_by').annotate(
            total_expense=Sum('expense__amount', output_field=models.DecimalField())
        )
        all_users = User.objects.all()
        context = {
            'expenses_group': expense_groups,
            'form': form,
            'all_users': all_users,
        }
        return render(request, self.template_name, context)

# class ExpenseDetailView(LoginRequiredMixin, View):
#     model = Expense
#     template_name = 'expenses_mate/expenses_detail.html'
#     login_url = 'expenses_mate:account_login'

#     def get(self, request, *args, **kwargs):
#         group_id = self.kwargs.get('group_id')
#         group = get_object_or_404(ExpenseGroup, group_id=group_id)
#         expenses = self.get_queryset(group)

#         user_totals = self.calculate_user_totals(group)

#         context = {
#             'expenses': expenses,
#             'user_totals': user_totals,
#             'form': ExpenseForm(),
#             'expenses_group': group
#         }
#         return render(request, self.template_name, context)

#     def get_queryset(self, group):
#         return Expense.objects.filter(group_id=group)

#     def calculate_user_totals(self, group):
#         return (
#             Expense.objects.filter(group_id=group)
#             .values('user_id__username')
#             .annotate(total_amount=Sum('amount'))
#             .order_by('user_id__username')
#         )

#     def post(self, request, *args, **kwargs):
#         group_id = self.kwargs.get('group_id')
#         group = get_object_or_404(ExpenseGroup, group_id=group_id) 
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             expense = form.save(commit=False)
#             expense.group_id = group
#             expense.user_id = request.user
#             expense.save()
#             return redirect('expenses_mate:expense_detail', group_id=group_id)

#         expenses = self.get_queryset(group)
#         user_totals = self.calculate_user_totals(group)
#         context = {
#             'expenses': expenses,
#             'user_totals': user_totals,
#             'form': form,
#         }
#         return render(request, self.template_name, context)
    
class ExpenseManageView(LoginRequiredMixin, FormView, ListView):
    template_name = 'expenses_mate/expenses_detail.html'
    form_class = ExpenseForm
    model = Expense
    context_object_name = 'expenses'

    def get_success_url(self):
        return reverse_lazy('expenses_mate:expense_detail', kwargs={'group_id': self.kwargs['group_id']})

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Expense.objects.filter(group_id=group_id)

    def get_form(self):
        form = super().get_form()
        form.instance.user_id = self.request.user
        return form

    def form_valid(self, form):
        group_id = self.kwargs['group_id']
        form.instance.group_id = get_object_or_404(ExpenseGroup, group_id=group_id)
        form.instance.user_id = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_id = self.kwargs['group_id']
        context['expenses'] = self.get_queryset()  # Set for ListView
        context['expenses_group'] = get_object_or_404(ExpenseGroup, group_id=group_id)
        context['user_totals'] = (
            Expense.objects.filter(group_id=group_id)
                .values('user_id__username')
                .annotate(total_amount=Sum('amount'))
                .order_by('user_id__username')
        )
        context['form'] = self.get_form()  # Add form for FormView
        return context

    def post(self, request, *args, **kwargs):
        if 'expense_id' in request.POST:
            expense = get_object_or_404(Expense, expense_id=request.POST['expense_id'])
            if 'delete' in request.POST:
                expense.delete()
            else:
                form = self.form_class(request.POST, instance=expense)
                if form.is_valid():
                    form.instance.user_id = expense.user_id
                    form.save()
                    return redirect(self.get_success_url())
                else:
                    return self.form_invalid(form)
        else:
            form = self.form_class(request.POST)
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return redirect(self.get_success_url())
    

class ShareExpenseGroupView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        expense_group = get_object_or_404(ExpenseGroup, group_id=kwargs['group_id'])
        
        form = ExpenseGroupForm(request.POST, instance=expense_group)
        
        if form.is_valid():
            expense_group = form.save()
            print("Form saved successfully with shared_with:", form.cleaned_data['shared_with'])
            return redirect('expenses_mate:expenses_list_create')
        else:
            print("Form errors:", form.errors)
            expenses = expense_group.expense_set.all()
            return render(request, 'expenses_mate/expenses_list.html', {
                'form': form,
                'expense_group': expense_group,
                'expenses': expenses
            })
            

class UpdateExpenseGroupView(LoginRequiredMixin, UpdateView):
    model = ExpenseGroup
    fields = ['title']

    def post(self, request, *args, **kwargs):
        expense_group = get_object_or_404(ExpenseGroup, group_id=kwargs['group_id'])

        expense_group.title = request.POST.get("title")
        expense_group.created_by = request.user

        # shared_with_ids = request.POST.getlist("shared_with")
        # expense_group.shared_with.set(shared_with_ids)

        expense_group.save()

        return redirect(reverse_lazy('expenses_mate:expenses_list_create'))


class UpdateExpenseView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['item_name', 'amount']

    def post(self, request, *args, **kwargs):
        expense = get_object_or_404(Expense, expense_id=kwargs['expense_id'])

        group_id = request.POST.get("group_id")
        expense.item_name = request.POST.get("item_name")
        expense.amount = request.POST.get("amount")

        expense.save()

        return redirect(reverse_lazy('expenses_mate:expense_detail', kwargs={'group_id': group_id}))
    